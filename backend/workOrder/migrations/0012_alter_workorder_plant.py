# Generated by Django 5.0.1 on 2024-09-30 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workOrder", "0011_rename_description_workorder_remark"),
    ]

    operations = [
        migrations.AlterField(
            model_name="workorder",
            name="plant",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]