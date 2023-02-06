from rest_framework import serializers

from core.models import *


class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = [
            "symbol",
            "long_name",
            "sector",
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
            "volume",
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
