# Generated by Django 4.1.5 on 2023-08-09 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_rename_name_task_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Date',
            field=models.DateField(default='2002-09-11'),
            preserve_default=False,
        ),
    ]
