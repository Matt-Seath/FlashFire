from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    cash = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)


class Stock(models.Model):
    symbol = models.CharField(max_length=255, unique=True)
    company = models.CharField(max_length=255)
    exchange = models.CharField(max_length=255)


class WatchList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="watchlist")


class StockHistory(models.Model):
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="history") 


class LatestTrade(models.Model):
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="latest")
    time = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=15)
    size = models.DecimalField(decimal_places=2, max_digits=15)


