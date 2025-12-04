from rest_framework.routers import DefaultRouter
from .views import ImpactRecordViewSet

router = DefaultRouter()
router.register(r"impact", ImpactRecordViewSet, basename="impact")

urlpatterns = router.urls