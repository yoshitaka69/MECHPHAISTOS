# Generated by Django 5.0.1 on 2024-03-10 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ceList", "0004_delete_function"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="machine",
            options={
                "ordering": ("companyCode",),
                "verbose_name": "Machine",
                "verbose_name_plural": "Machine",
            },
        ),
    ]