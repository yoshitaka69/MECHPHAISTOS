# Generated by Django 5.0.1 on 2024-03-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "junctionTable",
            "0003_masterdatatable_bomcode_masterdatatable_celist_id_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="masterdatatable",
            name="ceList_Id",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="constructionPeriod",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="countOfPM",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="laborCostOfPM",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="latestPM",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="nextEventDate",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="periodOfPM",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="situation",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="taskCode",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="taskName",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear10ago",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear10later",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear1ago",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear1later",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear2ago",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear2later",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear3ago",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear3later",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear4ago",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear4later",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear5ago",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear5later",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear6ago",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear6later",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear7ago",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear7later",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear8ago",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear8later",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear9ago",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="thisYear9later",
        ),
        migrations.RemoveField(
            model_name="masterdatatable",
            name="typeOfPM",
        ),
        migrations.AddField(
            model_name="masterdatatable",
            name="multiTask",
            field=models.BooleanField(default=False, verbose_name="multiTask"),
        ),
    ]