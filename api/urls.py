from rest_framework_nested import routers

from .views import *


router = routers.DefaultRouter()
router.register("", StockHistoryViewSet, basename="history")

urlpatterns = router.urls
