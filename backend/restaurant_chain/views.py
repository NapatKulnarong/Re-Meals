from rest_framework import viewsets
from .models import RestaurantChain
from .serializers import RestaurantChainSerializer

class RestaurantChainViewSet(viewsets.ModelViewSet):
    queryset = RestaurantChain.objects.all()
    serializer_class = RestaurantChainSerializer
    