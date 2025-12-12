from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("delivery", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="delivery",
            name="notes",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="delivery",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("in_transit", "In transit"),
                    ("delivered", "Delivered"),
                    ("cancelled", "Cancelled"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
    ]
