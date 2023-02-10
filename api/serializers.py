from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
        ]


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "user",
            "account_type",
            "cushion",
            "look_ahead_next_change",
            "accrued_cash",
            "available_funds",
            "buying_power",
            "equity_with_loan_value",
            "excess_liquidity",
            "full_available_funds",
            "full_excess_liquidity",
            "full_init_margin_req",
            "full_main_t_margin_req",
            "gross_position_value",
            "init_margin_req",
            "look_ahead_available_funds",
            "look_ahead_excess_liquidity",
            "look_ahead_init_margin_req",
            "look_ahead_main_margin_req",
            "main_t_margin_req",
            "net_liquidation",
            "total_cash_value",
            "last_updated",
        ]


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
