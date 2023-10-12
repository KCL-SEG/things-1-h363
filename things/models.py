from django.db import models
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=100, default='', unique=True)
    description = models.TextField(default='', unique=False)
    quantity = models.IntegerField(default=0, unique=False)


