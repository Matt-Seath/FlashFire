from rest_framework import routers
from django.urls import path, include
from .views import *


router = routers.DefaultRouter()
router.register("history", StockHistoryViewSet, basename="history")
router.register("account", AccountViewSet, basename="account")

urlpatterns = [
    path("", include(router.urls)),
    path("user/", include("user.urls")),
]
