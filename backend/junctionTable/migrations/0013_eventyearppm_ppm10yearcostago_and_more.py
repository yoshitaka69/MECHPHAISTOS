# Generated by Django 5.0.1 on 2024-04-21 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("junctionTable", "0012_delete_eventyearapm"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM10YearCostAgo",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="PPM10YearCostAgo",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM1YearCostAgo",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="PPM1YearCostAgo",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM2YearCostAgo",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="PPM2YearCostAgo",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM3YearCostAgo",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="PPM3YearCostAgo",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM4YearCostAgo",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="PPM4YearCostAgo",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM5YearCostAgo",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="PPM5YearCostAgo",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM6YearCostAgo",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="PPM6YearCostAgo",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM7YearCostAgo",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="PPM7YearCostAgo",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM8YearCostAgo",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="PPM8YearCostAgo",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="PPM9YearCostAgo",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                default=0.0,
                max_digits=10,
                null=True,
                verbose_name="PPM9YearCostAgo",
            ),
        ),
    ]