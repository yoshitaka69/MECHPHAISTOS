# Generated by Django 5.0.1 on 2024-08-18 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("test_app", "0005_product_unique_test_no"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="product",
            name="unique_test_no",
        ),
    ]
