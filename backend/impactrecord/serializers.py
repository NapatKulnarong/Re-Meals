from rest_framework import serializers
from .models import ImpactRecord


class ImpactRecordSerializer(serializers.ModelSerializer):
    # Explicitly define impact_id to ensure it's returned correctly
    impact_id = serializers.CharField(read_only=True)
    # Food field will return the food_id (primary key) as a string
    food = serializers.SerializerMethodField()
    
    def get_food(self, obj):
        # Return food_id as string to ensure consistent format
        return str(obj.food.food_id) if obj.food and hasattr(obj.food, 'food_id') else ""
    
    class Meta:
        model = ImpactRecord
        fields = [
            "impact_id",
            "meals_saved",
            "weight_saved_kg",
            "co2_reduced_kg",
            "impact_date",
            "food",
        ]