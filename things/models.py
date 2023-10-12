from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30, default='', unique=True)
    description = models.TextField(max_length=120,default='', unique=False)
    quantity = models.IntegerField(default=0, unique=False,range = (0,100))

class User(AbstractUser):
    x = 0
