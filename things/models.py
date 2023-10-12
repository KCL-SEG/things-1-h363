from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Thing(models.Model):
    name = models.CharField(max_length=30, default='', unique=True, blank=False)
    description = models.CharField(max_length=120, default='', unique=False, blank = True)
    quantity = models.IntegerField(validators=[
        MinValueValidator(0, message='Quantity must not be negative'),
        MaxValueValidator(100, message='Quantity must not be greater than 100')
    ])


