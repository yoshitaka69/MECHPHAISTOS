# Generated by Django 5.0.1 on 2024-08-18 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("junctionTable", "0020_alter_masterdatatable_bomcode_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="masterdatatable",
            name="ceListNo",
            field=models.CharField(
                blank=True,
                max_length=200,
                null=True,
                unique=True,
                verbose_name="ceListNo",
            ),
        ),
    ]
