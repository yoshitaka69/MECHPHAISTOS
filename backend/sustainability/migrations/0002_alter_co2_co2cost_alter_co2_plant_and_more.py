# Generated by Django 5.0.1 on 2024-03-16 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_plant"),
        ("sustainability", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="co2",
            name="co2Cost",
            field=models.DecimalField(
                blank=True,
                decimal_places=5,
                default=0.0,
                max_digits=15,
                null=True,
                verbose_name="co2Cost",
            ),
        ),
        migrations.AlterField(
            model_name="co2",
            name="plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="co2_plant",
                to="accounts.plant",
            ),
        ),
        migrations.AlterField(
            model_name="compressedair",
            name="plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="compAir_plant",
                to="accounts.plant",
            ),
        ),
        migrations.AlterField(
            model_name="electricityusage",
            name="plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="elec_plant",
                to="accounts.plant",
            ),
        ),
        migrations.AlterField(
            model_name="exhaustgas",
            name="plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exhaustGas_plant",
                to="accounts.plant",
            ),
        ),
        migrations.AlterField(
            model_name="purewater",
            name="plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pureWater_plant",
                to="accounts.plant",
            ),
        ),
        migrations.AlterField(
            model_name="stm",
            name="plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="stm_plant",
                to="accounts.plant",
            ),
        ),
        migrations.AlterField(
            model_name="wellwater",
            name="plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wellWater_plant",
                to="accounts.plant",
            ),
        ),
        migrations.AlterField(
            model_name="wwt",
            name="plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wwt_plant",
                to="accounts.plant",
            ),
        ),
    ]