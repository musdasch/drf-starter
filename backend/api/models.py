from django.db import models

class Task(models.Model):
	name 	= models.CharField(max_length=255);
	start 	= models.DateTimeField();
	end 	= models.DateTimeField(blank=True, null=True);