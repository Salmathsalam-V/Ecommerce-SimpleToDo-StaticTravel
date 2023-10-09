from django.db import models
class Place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to="picture")
    description=models.TextField()
    def __str__(self):
        return self.name
class Team(models.Model):
    name1=models.CharField(max_length=250)
    image1=models.ImageField(upload_to="picture")
    about=models.TextField()
    def __str__(self):
        return self.name1
# Create your models here.
