from django.utils import timezone
from rest_framework import serializers

from community.models import Community
from warehouse.models import Warehouse
from users.models import User
from .models import DonationRequest


class DonationRequestSerializer(serializers.ModelSerializer):
    request_id = serializers.CharField(read_only=True)
    community_id = serializers.PrimaryKeyRelatedField(
        queryset=Community.objects.all(),
        source="community",
        write_only=True,
        required=False,
        allow_null=True,
    )
    community_name = serializers.CharField()

    created_by_user_id = serializers.CharField(source='created_by.user_id', read_only=True, allow_null=True)

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
            "community_id",
            "created_by_user_id",
            "status",
        ]
        read_only_fields = ["created_at", "request_id", "created_by_user_id"]

    def create(self, validated_data):
        community_name = validated_data.get("community_name", "").strip()
        community_id = validated_data.get("community")
        
        # If community_id is provided, use it
        if community_id:
            community = community_id
        elif community_name:
            # Try to find existing community by name
            community = Community.objects.filter(name__iexact=community_name).first()
            
            # If not found, create a new community
            if not community:
                # Get or create a default warehouse (use first available or create one)
                warehouse = Warehouse.objects.first()
                if not warehouse:
                    # Create a default warehouse if none exists
                    from datetime import date, timedelta
                    warehouse = Warehouse.objects.create(
                        address="Default Warehouse",
                        capacity=1000.0,
                        stored_date=date.today(),
                        exp_date=date.today() + timedelta(days=365),
                    )
                
                # Create new community with auto-generated ID
                community = Community.objects.create(
                    name=community_name,
                    address=validated_data.get("recipient_address", community_name),
                    received_time=timezone.now(),
                    population=validated_data.get("people_count", 100),
                    warehouse_id=warehouse,
                )
        else:
            raise serializers.ValidationError({"community_name": "Community name is required."})
        
        validated_data["community"] = community
        # Set created_by from request context if available
        request = self.context.get('request')
        if request:
            # Try to get user from headers
            user_id = request.headers.get("X-USER-ID")
            if user_id:
                try:
                    user = User.objects.get(user_id=user_id)
                    validated_data["created_by"] = user
                except User.DoesNotExist:
                    pass
        return super().create(validated_data)

    def update(self, instance, validated_data):
        community_name = validated_data.get("community_name", "").strip()
        community_id = validated_data.get("community")
        
        # If community_id is provided, use it
        if community_id:
            community = community_id
        elif community_name:
            # Try to find existing community by name
            community = Community.objects.filter(name__iexact=community_name).first()
            
            # If not found, create a new community
            if not community:
                # Get or create a default warehouse (use first available or create one)
                warehouse = Warehouse.objects.first()
                if not warehouse:
                    # Create a default warehouse if none exists
                    from datetime import date, timedelta
                    warehouse = Warehouse.objects.create(
                        address="Default Warehouse",
                        capacity=1000.0,
                        stored_date=date.today(),
                        exp_date=date.today() + timedelta(days=365),
                    )
                
                # Create new community with auto-generated ID
                community = Community.objects.create(
                    name=community_name,
                    address=validated_data.get("recipient_address", instance.recipient_address),
                    received_time=timezone.now(),
                    population=validated_data.get("people_count", instance.people_count),
                    warehouse_id=warehouse,
                )
            validated_data["community"] = community
        
        return super().update(instance, validated_data)
