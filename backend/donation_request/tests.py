from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import DonationRequest, RequestItem


class DonationRequestAPITests(APITestCase):
    def test_create_request_with_items(self):
        payload = {
            "request_id": "REQ001",
            "title": "Fresh Meals",
            "community_name": "Community Alpha",
            "recipient_address": "123 Main St",
            "expected_delivery": "2025-12-31T10:00:00Z",
            "people_count": 50,
            "contact_phone": "0123456789",
            "notes": "",
            "items": [
                {"need_id": "NEED001", "item": "Cooked Rice", "quantity": 20, "urgency": "High"}
            ],
        }
        response = self.client.post(
            reverse("donation-request-list"), data=payload, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(DonationRequest.objects.filter(request_id="REQ001").exists())
        self.assertTrue(RequestItem.objects.filter(need_id="NEED001").exists())
