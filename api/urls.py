from rest_framework import routers
from django.urls import path, include
from rest_framework_nested.routers import NestedSimpleRouter
from .views import *


router = routers.DefaultRouter()

router.register("history", StockHistoryViewSet, basename="history")
router.register("account", AccountViewSet, basename="account")
router.register("watchlist", WatchlistViewSet, basename="watchlist")

watchlist_router = NestedSimpleRouter(router, r'watchlist', lookup='watchlist')
watchlist_router.register(r'items', WatchlistItemViewSet,
                          basename='watchlist-items')

urlpatterns = [
    path("", include(router.urls)),
    path("user/", include("user.urls")),
    path(r'', include(watchlist_router.urls)),
]
