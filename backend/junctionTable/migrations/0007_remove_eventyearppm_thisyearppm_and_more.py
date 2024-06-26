# Generated by Django 5.0.1 on 2024-04-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("junctionTable", "0006_eventyearppm"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eventyearppm",
            name="thisYearPPM",
        ),
        migrations.RemoveField(
            model_name="eventyearppm",
            name="thisYearPPM10Later",
        ),
        migrations.RemoveField(
            model_name="eventyearppm",
            name="thisYearPPM1Later",
        ),
        migrations.RemoveField(
            model_name="eventyearppm",
            name="thisYearPPM2Later",
        ),
        migrations.RemoveField(
            model_name="eventyearppm",
            name="thisYearPPM3Later",
        ),
        migrations.RemoveField(
            model_name="eventyearppm",
            name="thisYearPPM4Later",
        ),
        migrations.RemoveField(
            model_name="eventyearppm",
            name="thisYearPPM5Later",
        ),
        migrations.RemoveField(
            model_name="eventyearppm",
            name="thisYearPPM6Later",
        ),
        migrations.RemoveField(
            model_name="eventyearppm",
            name="thisYearPPM7Later",
        ),
        migrations.RemoveField(
            model_name="eventyearppm",
            name="thisYearPPM8Later",
        ),
        migrations.RemoveField(
            model_name="eventyearppm",
            name="thisYearPPM9Later",
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM10LaterCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=5,
                null=True,
                verbose_name="PPM10LaterCost",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM1LaterCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=5,
                null=True,
                verbose_name="PPM1LaterCost",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM2LaterCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=5,
                null=True,
                verbose_name="PPM2LaterCost",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM3LaterCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=5,
                null=True,
                verbose_name="PPM3LaterCost",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM4LaterCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=5,
                null=True,
                verbose_name="PPM4LaterCost",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM5LaterCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=5,
                null=True,
                verbose_name="PPM5LaterCost",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM6LaterCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=5,
                null=True,
                verbose_name="PPM6LaterCost",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM7LaterCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=5,
                null=True,
                verbose_name="PPM7LaterCost",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM8LaterCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=5,
                null=True,
                verbose_name="PPM8LaterCost",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM9LaterCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=5,
                null=True,
                verbose_name="PPM9LaterCost",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPMThisYearCost",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=5,
                null=True,
                verbose_name="PPMThisYearCost",
            ),
        ),
    ]
