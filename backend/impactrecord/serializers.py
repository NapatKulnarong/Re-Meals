from rest_framework import serializers
from .models import ImpactRecord


class ImpactRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpactRecord
        fields = "__all__"