from django.db import migrations, models


class Migration(migrations.Migration):
    """
    This migration ensures Django's state is in sync with the database.
    The actual column type change was done in 0006_fix_dropoff_time_data.
    """

    dependencies = [
        ("delivery", "0006_fix_dropoff_time_data"),
    ]

    operations = [
        # Just update Django's internal state - the column is already the correct type
        migrations.AlterField(
            model_name="delivery",
            name="dropoff_time",
            field=models.DateTimeField(),
        ),
    ]
