# Generated by Django 5.0.1 on 2024-08-09 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reliability", "0010_alter_reliability_failurecount_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reliability",
            name="componentCondition",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Component Condition",
            ),
        ),
        migrations.AddField(
            model_name="reliability",
            name="environmentCondition",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Environmental Conditions",
            ),
        ),
        migrations.AddField(
            model_name="reliability",
            name="failureCause",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Failure Cause"
            ),
        ),
        migrations.AddField(
            model_name="reliability",
            name="failureMode",
            field=models.CharField(
                blank=True,
                choices=[("pm03", "PM03"), ("pm04", "PM04")],
                max_length=50,
                null=True,
                verbose_name="Failure Mode",
            ),
        ),
        migrations.AddField(
            model_name="reliability",
            name="failureType",
            field=models.CharField(
                blank=True,
                choices=[
                    ("mechanical", "機械的故障"),
                    ("electrical", "電気的故障"),
                    ("both", "両方"),
                ],
                max_length=50,
                null=True,
                verbose_name="Failure Type",
            ),
        ),
        migrations.AddField(
            model_name="reliability",
            name="maintenanceFrequency",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Maintenance Frequency"
            ),
        ),
        migrations.AddField(
            model_name="reliability",
            name="maintenanceImpact",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Maintenance Impact"
            ),
        ),
        migrations.AddField(
            model_name="reliability",
            name="maintenanceMethod",
            field=models.CharField(
                blank=True,
                choices=[
                    ("inspection", "検査"),
                    ("periodic", "定期保全"),
                    ("parts_replacement", "部品交換"),
                    ("overhaul", "オーバーホール"),
                ],
                max_length=50,
                null=True,
                verbose_name="Maintenance Method",
            ),
        ),
        migrations.AddField(
            model_name="reliability",
            name="operationalCondition",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Operational Conditions",
            ),
        ),
        migrations.AlterField(
            model_name="reliability",
            name="failureCount",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Failure Count"
            ),
        ),
        migrations.AlterField(
            model_name="reliability",
            name="mtbf",
            field=models.IntegerField(blank=True, null=True, verbose_name="MTBF"),
        ),
        migrations.AlterField(
            model_name="reliability",
            name="mttf",
            field=models.IntegerField(blank=True, null=True, verbose_name="MTTF"),
        ),
        migrations.AlterField(
            model_name="reliability",
            name="mttr",
            field=models.IntegerField(blank=True, null=True, verbose_name="MTTR"),
        ),
        migrations.AlterField(
            model_name="reliability",
            name="totalOperatingTime",
            field=models.FloatField(
                blank=True, null=True, verbose_name="Total Operating Time"
            ),
        ),
    ]