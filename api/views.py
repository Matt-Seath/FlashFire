from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from core.models import StockInfo, StockHistory
from .serializers import *

from rest_framework.viewsets import ModelViewSet
# Create your views here.


class StockInfoViewSet(ModelViewSet):
    queryset = StockInfo.objects.values(*StockInfoSerializer.Meta.fields)
    serializer_class = StockInfoSerializer


class StockHistoryViewSet(viewsets.ViewSet):
    # queryset = StockInfo.objects.prefetch_related(
    #     "history").all().filter(pk="A2M.AX")
    # serializer_class = SimpleStockInfoSerializer
    def list(self, request):
        queryset = StockInfo.objects.prefetch_related(
            "history").all()
        stocks = []
        # for stock in queryset:
        print(queryset.history)
        print("")
        print("")
        #     history = qw.filter(stock=stock)
        #     data = [
        #     for record in history:
        #         data.append({
        #             "date": record.date,
        #             "open": record.open,
        #             "close": record.close,
        #             "high": record.high,
        #             "low": record.low,
        #         })
        #     stocks.append({
        #         "symbol": stock.symbol,
        #         "data": data
        #     })
        # return Response(stocks)


# class UserInRoom(APIView):
#     def get(self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         data = {
#             'code': self.request.session.get("room_code")
#         }
#         return JsonResponse(data, status=status.HTTP_200_OK)
