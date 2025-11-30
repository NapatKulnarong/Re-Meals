from rest_framework import viewsets
from rest_framework import filters
from django.utils.dateparse import parse_datetime
from rest_framework.response import Response

from .models import Restaurant, Donation
from .serializers import RestaurantSerializer, DonationSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def get_queryset(self):
        qs = Donation.objects.all()
        params = self.request.query_params

        restaurant_id = params.get("restaurant_id")
        status_param = params.get("status")
        date_from = params.get("date_from")
        date_to = params.get("date_to")

        if restaurant_id:
            qs = qs.filter(restaurant__restaurant_id=restaurant_id)

        if status_param is not None:
            status_param = status_param.lower()
            if status_param in ["true", "1"]:
                qs = qs.filter(status=True)
            elif status_param in ["false", "0"]:
                qs = qs.filter(status=False)
            else:
                return qs.none()   # invalid

        if date_from:
            qs = qs.filter(donated_at__gte=date_from)

        if date_to:
            qs = qs.filter(donated_at__lte=date_to)

        return qs

    # no change restaurant_id (FK)
    def update(self, request, *args, **kwargs):
        donation = self.get_object()

        # restaurant cannot be changed
        if "restaurant" in request.data:
            new_restaurant = request.data.get("restaurant")
            if new_restaurant != donation.restaurant.restaurant_id:
                return Response({"detail": "Cannot change restaurant of donation."}, status=400)

        # PK cannot be changed
        if "donation_id" in request.data:
            if request.data.get("donation_id") != donation.donation_id:
                return Response({"detail": "Cannot change donation_id."}, status=400)

        return super().update(request, *args, **kwargs)


    def partial_update(self, request, *args, **kwargs):
        donation = self.get_object()

        if "restaurant" in request.data:
            new_restaurant = request.data.get("restaurant")
            if new_restaurant != donation.restaurant.restaurant_id:
                return Response({"detail": "Cannot change restaurant of donation."}, status=400)

        if "donation_id" in request.data:
            if request.data.get("donation_id") != donation.donation_id:
                return Response({"detail": "Cannot change donation_id."}, status=400)

        return super().partial_update(request, *args, **kwargs)