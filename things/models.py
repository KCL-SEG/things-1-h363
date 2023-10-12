from django.db import models
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30, default='', unique=True, blank=False)
    description = models.TextField(max_length=120,default='', unique=False, blank=True)
    quantity = models.IntegerField(default=0, unique=False)

