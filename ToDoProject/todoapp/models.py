from django.db import models


class Task(models.Model):
    Task = models.CharField(max_length=120)
    Priority = models.IntegerField()
    Date=models.DateField()
    def __str__(self):
        return self.Task
# Create your models here.
