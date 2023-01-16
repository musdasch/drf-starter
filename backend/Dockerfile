FROM python:3.11

WORKDIR /app

RUN wget https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -P /usr/local/bin \
  && chmod +x /usr/local/bin/wait-for-it.sh

RUN pip install -U poetry

ARG INSTALL_DEV_DEPENDENCIES=false
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.create false \
  && if [ "$INSTALL_DEV_DEPENDENCIES" = "true" ]; then poetry install; else poetry install --no-dev; fi

COPY . /app

ENV DATABASE_PORT 5432

EXPOSE 80
CMD /bin/sh -c "wait-for-it.sh $DATABASE_HOST:$DATABASE_PORT -- ./manage.py migrate && ./manage.py collectstatic --noinput && uwsgi"

