# Generated by Django 5.0.1 on 2024-06-12 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reliability", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="WeibullData",
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
                ("failure_time", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
