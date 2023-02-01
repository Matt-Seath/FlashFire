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
