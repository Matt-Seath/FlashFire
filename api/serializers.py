from rest_framework import serializers

from core.models import *


class StockInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInfo
        fields = [
            "symbol",
            "average_volume",
            "sector",
            "long_business_summary",
            "volume",
            "market_cap",
            "current_price",
        ]
