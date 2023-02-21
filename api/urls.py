from rest_framework_nested import routers
from .views import *


router = routers.DefaultRouter()
router.register("history", StockHistoryViewSet, basename="history")
router.register("account", AccountViewSet, basename="account")
router.register("user", UserViewSet, basename="user")

urlpatterns = router.urls
