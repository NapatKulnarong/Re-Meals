from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, DonationViewSet

router = DefaultRouter()
router.register("restaurants", RestaurantViewSet, basename="restaurants")
router.register("donations", DonationViewSet)

urlpatterns = router.urls