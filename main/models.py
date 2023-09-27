# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    date_added = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)