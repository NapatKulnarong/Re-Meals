from django.db import migrations


def fix_dropoff_time_data(apps, schema_editor):
    # 🔒 ป้องกัน SQLite (ตอนรัน test)
    if schema_editor.connection.vendor != "postgresql":
        return

    # ✅ ทำเฉพาะ PostgreSQL เท่านั้น
    schema_editor.execute(
        """
        UPDATE delivery_delivery
        SET dropoff_time = dropoff_time::time
        WHERE dropoff_time IS NOT NULL;
        """
    )


class Migration(migrations.Migration):

    dependencies = [
        ("delivery", "0005_remove_delivery_delivered_quantity"),
    ]

    operations = [
        migrations.RunPython(fix_dropoff_time_data),
    ]