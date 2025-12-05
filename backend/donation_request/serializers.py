from rest_framework import serializers

from .models import DonationRequest, RequestItem


class RequestItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestItem
        fields = ["need_id", "item", "quantity", "urgency"]


class DonationRequestSerializer(serializers.ModelSerializer):
    items = RequestItemSerializer(many=True)

    class Meta:
        model = DonationRequest
        fields = [
            "request_id",
            "title",
            "community_name",
            "recipient_address",
            "expected_delivery",
            "people_count",
            "contact_phone",
            "notes",
            "created_at",
            "items",
        ]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        items_data = validated_data.pop("items", [])
        donation_request = DonationRequest.objects.create(**validated_data)

        for item in items_data:
            RequestItem.objects.create(request=donation_request, **item)

        return donation_request

    def update(self, instance, validated_data):
        items_data = validated_data.pop("items", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        if items_data is not None:
            instance.items.all().delete()
            for item in items_data:
                RequestItem.objects.create(request=instance, **item)

        return instance
