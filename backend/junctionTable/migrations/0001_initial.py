# Generated by Django 5.0.1 on 2024-03-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="JunctionTable",
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
                ("slug", models.SlugField()),
                (
                    "taskCode",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="taskCode"
                    ),
                ),
                (
                    "taskCost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        max_digits=5,
                        null=True,
                        verbose_name="taskCost",
                    ),
                ),
                (
                    "bomCode",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="bomCode"
                    ),
                ),
                (
                    "bomCost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        max_digits=5,
                        null=True,
                        verbose_name="bomCost",
                    ),
                ),
                (
                    "totalCost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        max_digits=5,
                        null=True,
                        verbose_name="totalCost",
                    ),
                ),
                (
                    "mostRecentPM",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        max_digits=5,
                        null=True,
                        verbose_name="mostRecentPM",
                    ),
                ),
                (
                    "mostRecentBomCost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        max_digits=5,
                        null=True,
                        verbose_name="mostRecentBomCost",
                    ),
                ),
            ],
            options={
                "verbose_name": "Junction Table",
                "verbose_name_plural": "Junction Table",
                "ordering": ("taskCode",),
            },
        ),
    ]