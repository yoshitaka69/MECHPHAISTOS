# Generated by Django 5.0.1 on 2024-10-13 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("simulation", "0002_basesimulation_no1simulation_no2simulation_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="no1simulation",
            name="multiTasking",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="thisYear",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="thisYear10Later",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="thisYear1Later",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="thisYear2Later",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="thisYear3Later",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="thisYear4Later",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="thisYear5Later",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="thisYear6Later",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="thisYear7Later",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="thisYear8Later",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="thisYear9Later",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="totalCost",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="typicalNextEventDate",
        ),
        migrations.RemoveField(
            model_name="no1simulation",
            name="typicalSituation",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="multiTasking",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="thisYear",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="thisYear10Later",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="thisYear1Later",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="thisYear2Later",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="thisYear3Later",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="thisYear4Later",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="thisYear5Later",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="thisYear6Later",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="thisYear7Later",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="thisYear8Later",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="thisYear9Later",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="totalCost",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="typicalNextEventDate",
        ),
        migrations.RemoveField(
            model_name="no2simulation",
            name="typicalSituation",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="multiTasking",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="thisYear",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="thisYear10Later",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="thisYear1Later",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="thisYear2Later",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="thisYear3Later",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="thisYear4Later",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="thisYear5Later",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="thisYear6Later",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="thisYear7Later",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="thisYear8Later",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="thisYear9Later",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="totalCost",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="typicalNextEventDate",
        ),
        migrations.RemoveField(
            model_name="no3simulation",
            name="typicalSituation",
        ),
        migrations.AddField(
            model_name="no1simulation",
            name="PMType",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="no1simulation",
            name="bomCode",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="no1simulation",
            name="bomCost",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="no1simulation",
            name="totalLaborCost",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="no2simulation",
            name="PMType",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="no2simulation",
            name="bomCode",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="no2simulation",
            name="bomCost",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="no2simulation",
            name="totalLaborCost",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="no3simulation",
            name="PMType",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="no3simulation",
            name="bomCode",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="no3simulation",
            name="bomCost",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="no3simulation",
            name="totalLaborCost",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="no1simulation",
            name="equipment",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no1simulation",
            name="machineName",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no1simulation",
            name="plant",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no1simulation",
            name="taskListNo",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no1simulation",
            name="taskOfPeriod",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="no1simulation",
            name="typicalLatestDate",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="no1simulation",
            name="typicalTaskName",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no2simulation",
            name="equipment",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no2simulation",
            name="machineName",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no2simulation",
            name="plant",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no2simulation",
            name="taskListNo",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no2simulation",
            name="taskOfPeriod",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="no2simulation",
            name="typicalLatestDate",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="no2simulation",
            name="typicalTaskName",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no3simulation",
            name="equipment",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no3simulation",
            name="machineName",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no3simulation",
            name="plant",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no3simulation",
            name="taskListNo",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="no3simulation",
            name="taskOfPeriod",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="no3simulation",
            name="typicalLatestDate",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="no3simulation",
            name="typicalTaskName",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name="BaseSimulation",
        ),
    ]