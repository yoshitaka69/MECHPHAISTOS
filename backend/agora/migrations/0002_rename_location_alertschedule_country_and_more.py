# Generated by Django 5.0.1 on 2024-04-30 04:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agora", "0001_initial"),
        ("spareParts", "0017_remove_spareparts_inventoryturnover_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="alertschedule",
            old_name="location",
            new_name="country",
        ),
        migrations.AlterField(
            model_name="alertschedule",
            name="partsName",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="alertSchedule_partsName",
                to="spareParts.spareparts",
            ),
        ),
    ]
