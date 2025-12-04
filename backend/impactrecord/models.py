from django.db import models

# Create your models here.
from fooditem.models import FoodItem


class ImpactRecord(models.Model):
    impact_id = models.CharField(max_length=10, primary_key=True)

    meals_saved = models.FloatField()
    weight_saved_kg = models.FloatField()
    co2_reduced_kg = models.FloatField()

    impact_date = models.DateField(auto_now_add=True)

    food = models.OneToOneField(
        FoodItem,
        on_delete=models.CASCADE,
        related_name="impact"
    )

    class Meta:
        db_table = "impact_record"

    def __str__(self):
        return f"ImpactRecord {self.impact_id}"