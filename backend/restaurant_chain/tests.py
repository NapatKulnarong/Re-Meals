from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .models import RestaurantChain


class RestaurantChainAPITests(APITestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_chain(self):
        payload = {"chain_id": "CHAIN10", "chain_name": "New Chain"}
        res = self.client.post("/api/restaurant-chains/", payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(RestaurantChain.objects.filter(chain_id="CHAIN10").exists())

    def test_list_chains(self):
        RestaurantChain.objects.create(chain_id="CHAIN11", chain_name="Chain 11")
        res = self.client.get("/api/restaurant-chains/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

    def test_delete_chain(self):
        chain = RestaurantChain.objects.create(chain_id="CHAIN12", chain_name="Chain 12")
        res = self.client.delete(f"/api/restaurant-chains/{chain.chain_id}/")
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(RestaurantChain.objects.filter(chain_id="CHAIN12").exists())
