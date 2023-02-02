from rest_framework_nested import routers

from .views import *


router = routers.DefaultRouter()
router.register("", StockHistoryViewSet)

urlpatterns = router.urls
