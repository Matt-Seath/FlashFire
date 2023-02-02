from .views import index
from rest_framework_nested import routers

from api.views import StockInfoViewSet

router = routers.DefaultRouter()
router.register("", StockInfoViewSet)

urlpatterns = router.urls
