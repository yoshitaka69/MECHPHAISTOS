# Generated by Django 5.0.1 on 2024-03-14 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        ("taskList", "0003_alter_tasklist_constructionperiod_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tasklist",
            name="companyCode",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="taskList_companyCode",
                to="accounts.companycode",
            ),
        ),
    ]