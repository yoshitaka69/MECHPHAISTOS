# Generated by Django 5.0.1 on 2024-04-07 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nearMiss", "0005_remove_safetyindicators_actionitems_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nearmiss",
            name="solvedActionItems",
            field=models.BooleanField(default=False, verbose_name="solvedActionItems"),
        ),
    ]
