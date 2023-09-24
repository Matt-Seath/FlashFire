from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet

from core.models import *
from .serializers import *


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.get(pk=1)
#     serializer_class = UserSerializer
class WatchlistItemViewSet(ModelViewSet):
    queryset = WatchlistItem.objects.filter(watchlist_id=1)
    serializer_class = WatchlistItemSerializer


class WatchlistViewSet(ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer

    def list(self, request, *args, **kwargs):
        user = request.user
        print(user)
        watchlists = self.queryset.filter(user_id=1)
        serialized_data = self.get_serializer(watchlists, many=True).data

        return Response(serialized_data)


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.filter(user_id=1)


class StockInfoViewSet(ModelViewSet):
    queryset = StockInfo.objects.values(*StockInfoSerializer.Meta.fields)
    serializer_class = StockInfoSerializer


class StockHistoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = StockInfo.objects.prefetch_related(Prefetch(
            "history", queryset=StockHistory.objects.filter(
                date__gt="2023-1-1", date__lt="2023-8-10"))).only(
            "symbol", "long_name", "sector").order_by("symbol")[:4]
        stocks = []
        for stock in queryset:
            history = stock.history.all()
            data = []
            for record in history:
                data.append([
                    record.date,
                    record.open,
                    record.close,
                    record.high,
                    record.low,
                    record.volume,
                ])
            stocks.append({
                "symbol": stock.symbol,
                "long_name": stock.long_name,
                "sector": stock.sector,
                "history": data
            })

        return Response(stocks)
