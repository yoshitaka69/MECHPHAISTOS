# Generated by Django 5.0.1 on 2024-03-25 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("spareParts", "0013_alter_spareparts_bomcode_and_more"),
        ("taskList", "0013_tasklist_tasklistno"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tasklist",
            name="bomCodeCost",
        ),
        migrations.AddField(
            model_name="tasklist",
            name="bomCost",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="taskList_bomCost",
                to="spareParts.bomlist",
            ),
        ),
    ]