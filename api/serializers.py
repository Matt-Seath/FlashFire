from rest_framework import serializers

from core.models import *


class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = [
            "symbol",
            "long_name",
            "sector",
            "average_volume",
            "volume",
            "market_cap",
            "current_price",
            "last_updated",
        ]


class SimpleStockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = [
            "symbol",
            "long_name",
            "sector",
        ]


class StockHistorySerializer(serializers.ModelSerializer):
    stock = SimpleStockInfoSerializer()

    class Meta:
        model = StockHistory
        fields = [
            "stock",
            "date",
            "open",
            "close",
            "high",
            "low",
            "close",
        ]
