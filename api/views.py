from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Prefetch
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet


from core.models import *
from .serializers import *


# class UserViewSet(ModelViewSet):
#     queryset = User.objects.get(pk=1)
#     serializer_class = UserSerializer

class WatchlistItemViewSet(ModelViewSet):

    def get_serializer_class(self):
        if self.request.method == "POST":
            return AddWatchlistItemSerializer
        return WatchlistItemSerializer

    def get_serializer_context(self):
        return {"watchlist": self.kwargs["watchlist_pk"]}

    def get_queryset(self):
        return WatchlistItem.objects \
            .filter(watchlist=self.kwargs["watchlist_pk"]) \
            .select_related("stock")


class WatchlistViewSet(ModelViewSet):
    queryset = Watchlist.objects.prefetch_related("items__stock").all()
    serializer_class = WatchlistSerializer


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
