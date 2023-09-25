from rest_framework import serializers
from core.models import *


class WatchlistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchlistItem
        fields = [
            "watchlist_id",
            "stock_id",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation['stock_id']


class WatchlistSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = WatchlistItemSerializer(many=True, read_only=True)

    class Meta:
        model = Watchlist
        fields = [
            "id",
            "user_id",
            "name",
            "items",
        ]


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
            "username",
        ]


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            "id",
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
            "look_ahead_main_t_margin_req",
            "main_t_margin_req",
            "net_liquidation",
            "total_cash_value",
            "last_updated",
        ]


class SimpleAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            "id",
            "account_type",
            "accrued_cash",
            "available_funds",
            "buying_power",
            "excess_liquidity",
            "full_available_funds",
            "full_excess_liquidity",
            "gross_position_value",
            "net_liquidation",
            "total_cash_value",
            "last_updated",
        ]


class UserSerializer(serializers.ModelSerializer):
    accounts = SimpleAccountSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "accounts",
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
