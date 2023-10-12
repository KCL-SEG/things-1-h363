from django.db import models
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=100, default='', Unique=True)
    description = models.TextField(default='', Unique=False)
    quantity = models.IntegerField(default=0, Unique=False)


