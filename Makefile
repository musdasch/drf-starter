SHELL:=/bin/sh

.PHONY: dbshell
dbshell: ## Start a psql shell
	@docker-compose exec db psql -Uadmin admin

.PHONY: debug-backend
debug-backend: ## start a backend container with service ports for debugging
	@docker-compose stop backend
	@echo "run `./manage.py runserver 0:80` to start debug server"
	@docker-compose run --user root --use-aliases --service-ports backend bash
