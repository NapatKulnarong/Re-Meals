from django.db import migrations


def fix_dropoff_time_data(apps, schema_editor):
    """
    Convert interval dropoff_time values to proper timestamp values.
    For each delivery, add the interval to the pickup_time to get the dropoff_time.
    Uses raw SQL since Django ORM can't handle interval to timestamp conversion.
    """
    # Add a temporary column to store the converted timestamp
    schema_editor.execute("""
        ALTER TABLE delivery_delivery
        ADD COLUMN dropoff_time_temp timestamp with time zone;
    """)

    # Calculate the new dropoff_time as pickup_time + interval
    schema_editor.execute("""
        UPDATE delivery_delivery
        SET dropoff_time_temp = pickup_time + dropoff_time::interval
        WHERE dropoff_time IS NOT NULL;
    """)

    # Drop the old interval column
    schema_editor.execute("""
        ALTER TABLE delivery_delivery
        DROP COLUMN dropoff_time;
    """)

    # Rename the temp column to dropoff_time
    schema_editor.execute("""
        ALTER TABLE delivery_delivery
        RENAME COLUMN dropoff_time_temp TO dropoff_time;
    """)


def reverse_migration(apps, schema_editor):
    """
    Reverse is not implemented as we cannot reliably convert back.
    """
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("delivery", "0005_remove_delivery_delivered_quantity"),
    ]

    operations = [
        migrations.RunPython(fix_dropoff_time_data, reverse_migration),
    ]
