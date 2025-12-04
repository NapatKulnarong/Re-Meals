from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant_chain", "0001_initial"),
        ("restaurants", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="chain",
            field=models.ForeignKey(
                blank=True,
                db_column="chain_id",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="restaurants",
                to="restaurant_chain.restaurantchain",
            ),
        ),
    ]
