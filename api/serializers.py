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


class StockHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockHistory
        fields = [
            "date",
            "open",
            "close",
            "high",
            "low",
            "close",
        ]


class SimpleStockInfoSerializer(serializers.ModelSerializer):
    data = StockHistorySerializer(many=True, read_only=True)

    class Meta:
        model = StockInfo
        fields = [
            "symbol",
            "long_name",
            "sector",
            "data",
        ]
