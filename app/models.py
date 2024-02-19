from django.db import models

# Create your models here.
class ModelReg(models.Model):
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.CharField(max_length=10)

class ModelPerson(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    profession = models.CharField(max_length=15)
    age = models.IntegerField()

class Img(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='app/static/imgs')