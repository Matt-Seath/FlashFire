from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet

from core.models import StockInfo, StockHistory
from .serializers import *


class StockInfoViewSet(ModelViewSet):
    queryset = StockInfo.objects.values(*StockInfoSerializer.Meta.fields)
    serializer_class = StockInfoSerializer


class StockHistoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = StockInfo.objects.prefetch_related(Prefetch(
            "history", queryset=StockHistory.objects.filter(
                date__gt="2023-1-1", date__lt="2023-1-10"))).only(
            "symbol", "long_name", "sector").order_by("symbol")[:4]
        stocks = []
        for stock in queryset:
            history = stock.history.all()
            data = []
            for record in history:
                data.append({
                    "date": record.date,
                    "open": record.open,
                    "close": record.close,
                    "high": record.high,
                    "low": record.low,
                })
            stocks.append({
                "symbol": stock.symbol,
                "long_name": stock.long_name,
                "sector": stock.sector,
                "history": data
            })

        return Response(stocks)


# class UserInRoom(APIView):
#     def get(self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         data = {
#             'code': self.request.session.get("room_code")
#         }
#         return JsonResponse(data, status=status.HTTP_200_OK)
