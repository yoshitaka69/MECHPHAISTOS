# Generated by Django 5.0.1 on 2024-03-25 05:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_plant"),
        ("ceList", "0008_machine_alter_celist_machinename"),
        ("spareParts", "0012_alter_bomlist_bomcode_alter_bomlist_bomcost_and_more"),
        ("taskList", "0010_tasklistpm04_constructionperiod"),
    ]

    operations = [
        migrations.CreateModel(
            name="TypicalTaskList",
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
                    "taskCode",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="taskCode"
                    ),
                ),
                (
                    "typicalTask",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="typicalTask",
                    ),
                ),
                (
                    "typicalTaskCost",
                    models.DecimalField(
                        blank=True,
                        decimal_places=5,
                        default=0.0,
                        max_digits=10,
                        null=True,
                        verbose_name="typicalTaskCost",
                    ),
                ),
                (
                    "typicalLatestDate",
                    models.DateField(
                        blank=True, null=True, verbose_name="typicalLatestDate"
                    ),
                ),
                (
                    "typicalConstPeriod",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="typicalConstPeriod"
                    ),
                ),
                (
                    "typicalNextEventDate",
                    models.DateField(
                        blank=True, null=True, verbose_name="typicalNextEventDate"
                    ),
                ),
                (
                    "multiTasking",
                    models.BooleanField(default=False, verbose_name="multiTasking"),
                ),
            ],
            options={
                "verbose_name": "Typical Task List",
                "verbose_name_plural": "Typical Task List",
                "ordering": ("taskCode",),
            },
        ),
        migrations.AlterField(
            model_name="tasklistpm02",
            name="machineName",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="taskListPM02_machineName",
                to="ceList.machine",
            ),
        ),
        migrations.AlterField(
            model_name="tasklistpm03",
            name="machineName",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="taskListPM03_machineName",
                to="ceList.machine",
            ),
        ),
        migrations.AlterField(
            model_name="tasklistpm04",
            name="machineName",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="taskListPM04_machineName",
                to="ceList.machine",
            ),
        ),
        migrations.AlterField(
            model_name="tasklistpm05",
            name="machineName",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="taskListPM05_machineName",
                to="ceList.machine",
            ),
        ),
        migrations.CreateModel(
            name="TaskList",
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
                    "thisYear",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="thisYear"
                    ),
                ),
                (
                    "thisYear1later",
                    models.BooleanField(default=False, verbose_name="thisYear1later"),
                ),
                (
                    "thisYear2later",
                    models.BooleanField(default=False, verbose_name="thisYear2later"),
                ),
                (
                    "thisYear3later",
                    models.BooleanField(default=False, verbose_name="thisYear3later"),
                ),
                (
                    "thisYear4later",
                    models.BooleanField(default=False, verbose_name="thisYear4later"),
                ),
                (
                    "thisYear5later",
                    models.BooleanField(default=False, verbose_name="thisYear5later"),
                ),
                (
                    "thisYear6later",
                    models.BooleanField(default=False, verbose_name="thisYear6later"),
                ),
                (
                    "thisYear7later",
                    models.BooleanField(default=False, verbose_name="thisYear7later"),
                ),
                (
                    "thisYear8later",
                    models.BooleanField(default=False, verbose_name="thisYear8later"),
                ),
                (
                    "thisYear9later",
                    models.BooleanField(default=False, verbose_name="thisYear9later"),
                ),
                (
                    "thisYear10later",
                    models.BooleanField(default=False, verbose_name="thisYear10later"),
                ),
                (
                    "bomCode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_bomCode",
                        to="spareParts.bomlist",
                    ),
                ),
                (
                    "bomCodeCost",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_bomCodeCost",
                        to="spareParts.bomlist",
                    ),
                ),
                (
                    "companyCode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_companyCode",
                        to="accounts.companycode",
                    ),
                ),
                (
                    "equipment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_equipment",
                        to="ceList.equipment",
                    ),
                ),
                (
                    "machineName",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_equipment",
                        to="ceList.machine",
                    ),
                ),
                (
                    "plant",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_plant",
                        to="accounts.plant",
                    ),
                ),
                (
                    "multiTasking",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_multiTasking",
                        to="taskList.typicaltasklist",
                    ),
                ),
                (
                    "typicalConstPeriod",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_typicalConstPeriod",
                        to="taskList.typicaltasklist",
                    ),
                ),
                (
                    "typicalLatestDate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_typicalLatestDate",
                        to="taskList.typicaltasklist",
                    ),
                ),
                (
                    "typicalNextEventDate",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_typicalNextEventDate",
                        to="taskList.typicaltasklist",
                    ),
                ),
                (
                    "typicalSituation",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_typicalSituation",
                        to="taskList.typicaltasklist",
                    ),
                ),
                (
                    "typicalTask",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_typicalTask",
                        to="taskList.typicaltasklist",
                    ),
                ),
                (
                    "typicalTaskCost",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="taskList_typicalTaskCost",
                        to="taskList.typicaltasklist",
                    ),
                ),
            ],
            options={
                "verbose_name": "Task List",
                "verbose_name_plural": "Task List",
                "ordering": ("companyCode",),
            },
        ),
    ]