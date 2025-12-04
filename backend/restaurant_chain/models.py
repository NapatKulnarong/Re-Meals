from django.db import models

class RestaurantChain(models.Model):
    chain_id = models.CharField(max_length=10, primary_key=True)
    chain_name = models.CharField(max_length=100)

    def __str__(self):
        return self.chain_name
