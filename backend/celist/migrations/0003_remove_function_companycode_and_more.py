# Generated by Django 5.0.1 on 2024-03-10 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_companyname_options_alter_customuser_options"),
        (
            "ceList",
            "0002_alter_celist_companycode_alter_equipment_companycode_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="function",
            name="companyCode",
        ),
        migrations.RemoveField(
            model_name="function",
            name="companyName",
        ),
        migrations.RemoveField(
            model_name="celist",
            name="function",
        ),
        migrations.RemoveField(
            model_name="celist",
            name="locationNo",
        ),
        migrations.CreateModel(
            name="Machine",
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
                (
                    "machineName",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="machineName",
                    ),
                ),
                (
                    "spareMachineLocationNo",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="spareMachineLocationNo",
                    ),
                ),
                (
                    "companyCode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="function_companyCode",
                        to="accounts.companycode",
                    ),
                ),
                (
                    "companyName",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="function_companyName",
                        to="accounts.companyname",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="celist",
            name="machineName",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ceList_machine",
                to="ceList.machine",
            ),
        ),
    ]