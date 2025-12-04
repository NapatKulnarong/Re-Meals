from rest_framework.routers import DefaultRouter
from .views import RestaurantChainViewSet

router = DefaultRouter()
router.register(r"restaurant-chains", RestaurantChainViewSet, basename="restaurant-chain")

urlpatterns = router.urls
