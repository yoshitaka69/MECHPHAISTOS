# Generated by Django 5.0.1 on 2024-04-14 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spareParts", "0015_sparepartsmanagement"),
    ]

    operations = [
        migrations.AddField(
            model_name="spareparts",
            name="summedPartsCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="summedPartsCost",
            ),
        ),
        migrations.AlterField(
            model_name="spareparts",
            name="numberOf",
            field=models.PositiveIntegerField(
                blank=True, default=0, null=True, verbose_name="numberOf"
            ),
        ),
    ]
