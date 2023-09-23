# Create your models here.
from django.db import models

class Product(models.Model):
    date_added = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
