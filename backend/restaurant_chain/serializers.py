from rest_framework import serializers
from .models import RestaurantChain

class RestaurantChainSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantChain
        fields = ['chain_id', 'chain_name']