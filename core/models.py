from django.db import models

# Create your models here.

class Username(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    cash = models.DecimalField(default=0.00)

class Stock(models.Model):
    symbol = models.CharField(max_length=255, unigue=True)
    company = models.CharField(max_length=255),
    exchange = models.CharField(max_length=255)

