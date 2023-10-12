from django.db import models
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField(default='')
    quantity = models.IntegerField(default=0)


