from django.db import models


class DonationRequest(models.Model):
    request_id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=120)
    community_name = models.CharField(max_length=120)
    recipient_address = models.CharField(max_length=300)
    expected_delivery = models.DateTimeField()
    people_count = models.PositiveIntegerField()
    contact_phone = models.CharField(max_length=30, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "donation_request"
        ordering = ["-created_at"]

    def __str__(self):
        return f"DonationRequest {self.request_id}"


class RequestItem(models.Model):
    URGENCY_CHOICES = [
        ("Normal", "Normal"),
        ("High", "High"),
        ("Critical", "Critical"),
    ]

    need_id = models.CharField(max_length=12, primary_key=True)
    request = models.ForeignKey(
        DonationRequest,
        on_delete=models.CASCADE,
        related_name="items",
    )
    item = models.CharField(max_length=150)
    quantity = models.PositiveIntegerField()
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES, default="Normal")

    class Meta:
        db_table = "donation_request_item"

    def __str__(self):
        return f"{self.item} ({self.quantity})"
