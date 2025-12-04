# Create your views here.
from rest_framework import viewsets
from .models import ImpactRecord
from .serializers import ImpactRecordSerializer


class ImpactRecordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ImpactRecord.objects.all()
    serializer_class = ImpactRecordSerializer