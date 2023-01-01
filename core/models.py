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

class StockPriceMinute(models.Model):
    open = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    high = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    low = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    close = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    volume = models.DecimalField(default=0.00, decimal_places=2, max_digits=15)
    datetime = models.DateTimeField(auto_now_add=True)

class WatchList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="watchlist")


class StockHistory(models.Model):
    stock_id = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name="history") 