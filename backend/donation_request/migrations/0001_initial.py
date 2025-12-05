import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DonationRequest",
            fields=[
                ("request_id", models.CharField(max_length=10, primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=120)),
                ("community_name", models.CharField(max_length=120)),
                ("recipient_address", models.CharField(max_length=300)),
                ("expected_delivery", models.DateTimeField()),
                ("people_count", models.PositiveIntegerField()),
                ("contact_phone", models.CharField(blank=True, max_length=30)),
                ("notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "db_table": "donation_request",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="RequestItem",
            fields=[
                ("need_id", models.CharField(max_length=12, primary_key=True, serialize=False)),
                ("item", models.CharField(max_length=150)),
                ("quantity", models.PositiveIntegerField()),
                (
                    "urgency",
                    models.CharField(
                        choices=[("Normal", "Normal"), ("High", "High"), ("Critical", "Critical")],
                        default="Normal",
                        max_length=20,
                    ),
                ),
                (
                    "request",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="donation_request.donationrequest",
                    ),
                ),
            ],
            options={
                "db_table": "donation_request_item",
            },
        ),
    ]
