# Generated by Django 5.0.1 on 2024-03-07 16:54

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        ("taskList", "0001_initial"),
    ]

    operations = [
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
                ("slug", models.SlugField()),
                (
                    "taskCode",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="taskCode"
                    ),
                ),
                (
                    "taskName",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="taskName"
                    ),
                ),
                (
                    "taskOfPM",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="taskOfPM"
                    ),
                ),
                (
                    "laborCostOfPM",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0.0,
                        max_digits=5,
                        null=True,
                        verbose_name="laborCostOfPM",
                    ),
                ),
                (
                    "countOfPM",
                    models.PositiveSmallIntegerField(
                        blank=True, default=0, null=True, verbose_name="countOfPM"
                    ),
                ),
                (
                    "latestPM",
                    models.DateField(blank=True, null=True, verbose_name="latestPM"),
                ),
                (
                    "periodOfPM",
                    models.DateField(
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="periodOfPM",
                    ),
                ),
                (
                    "typeOfMaintenance",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="typeOfMaintenance",
                    ),
                ),
                (
                    "constructionPeriod",
                    models.DateField(
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="constructionPeriod",
                    ),
                ),
                (
                    "nextEventDate",
                    models.DateField(
                        blank=True, null=True, verbose_name="nextEventDate"
                    ),
                ),
                (
                    "situation",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="situation"
                    ),
                ),
                (
                    "thisYear10ago",
                    models.BooleanField(default=False, verbose_name="thisYear10ago"),
                ),
                (
                    "thisYear9ago",
                    models.BooleanField(default=False, verbose_name="thisYear9ago"),
                ),
                (
                    "thisYear8ago",
                    models.BooleanField(default=False, verbose_name="thisYear8ago"),
                ),
                (
                    "thisYear7ago",
                    models.BooleanField(default=False, verbose_name="thisYear7ago"),
                ),
                (
                    "thisYear6ago",
                    models.BooleanField(default=False, verbose_name="thisYear6ago"),
                ),
                (
                    "thisYear5ago",
                    models.BooleanField(default=False, verbose_name="thisYear5ago"),
                ),
                (
                    "thisYear4ago",
                    models.BooleanField(default=False, verbose_name="thisYear4ago"),
                ),
                (
                    "thisYear3ago",
                    models.BooleanField(default=False, verbose_name="thisYear3ago"),
                ),
                (
                    "thisYear2ago",
                    models.BooleanField(default=False, verbose_name="thisYear2ago"),
                ),
                (
                    "thisYear1ago",
                    models.BooleanField(default=False, verbose_name="thisYear1ago"),
                ),
                ("thisYear", models.CharField(max_length=200, verbose_name="thisYear")),
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
                    "companyCode",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.company",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Task",
        ),
    ]