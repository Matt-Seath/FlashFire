from rest_framework import generics, status
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


class StockHistoryViewSet(ModelViewSet):
    queryset = StockHistory.objects.all().select_related("stock").filter(id__lt=24222)
    serializer_class = StockHistorySerializer

# class UserInRoom(APIView):
#     def get(self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         data = {
#             'code': self.request.session.get("room_code")
#         }
#         return JsonResponse(data, status=status.HTTP_200_OK)
