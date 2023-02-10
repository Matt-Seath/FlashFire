from rest_framework_nested import routers

from .views import *


router = routers.DefaultRouter()
router.register("history", StockHistoryViewSet, basename="history")
router.register("account", StockHistoryViewSet, basename="history")

urlpatterns = router.urls
