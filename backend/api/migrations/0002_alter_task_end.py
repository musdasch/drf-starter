# Generated by Django 4.1.5 on 2023-01-17 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.DateTimeField(blank=True),
        ),
    ]
