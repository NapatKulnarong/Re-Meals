from rest_framework.routers import DefaultRouter

from .views import DonationRequestViewSet


router = DefaultRouter()
router.register(r"donation-requests", DonationRequestViewSet, basename="donation-request")

urlpatterns = router.urls
