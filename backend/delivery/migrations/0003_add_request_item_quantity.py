from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("donation_request", "0001_initial"),
        ("delivery", "0002_add_status_notes"),
    ]

    operations = [
        migrations.AddField(
            model_name="delivery",
            name="delivered_quantity",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="delivery",
            name="request_item",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.SET_NULL,
                related_name="deliveries",
                to="donation_request.requestitem",
            ),
        ),
    ]
