from django.contrib import admin
from .models import RestaurantChain

@admin.register(RestaurantChain)
class RestaurantChainAdmin(admin.ModelAdmin):
    list_display = ("chain_id", "chain_name")
    search_fields = ("chain_name",)
    