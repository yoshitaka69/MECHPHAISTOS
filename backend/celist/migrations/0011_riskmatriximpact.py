# Generated by Django 5.0.1 on 2024-06-23 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_plant"),
        ("ceList", "0010_riskmatrixpossibility"),
    ]

    operations = [
        migrations.CreateModel(
            name="RiskMatrixImpact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "levelSetValue",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="levelSetValue",
                    ),
                ),
                (
                    "x",
                    models.FloatField(
                        blank=True, default=0, null=True, verbose_name="x"
                    ),
                ),
                (
                    "y",
                    models.FloatField(
                        blank=True, default=0, null=True, verbose_name="y"
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "companyCode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="riskMatrixImpact_companyCode",
                        to="accounts.companycode",
                    ),
                ),
                (
                    "companyName",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="riskMatrixImpact_companyName",
                        to="accounts.companyname",
                    ),
                ),
            ],
            options={
                "verbose_name": "Risk Matrix Impact",
                "verbose_name_plural": "Risk Matrix Impact",
                "ordering": ("-timestamp",),
            },
        ),
    ]