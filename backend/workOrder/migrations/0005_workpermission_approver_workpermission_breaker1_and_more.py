# Generated by Django 5.0.1 on 2024-08-24 00:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workOrder", "0004_alter_workpermission_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="workpermission",
            name="approver",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="breaker1",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="breaker2",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="breaker3",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="breaker4",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="breaker5",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="contractor",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="createdAt",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="gasDetection",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="onSiteSafety",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="oxygenDeficiency",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="updatedAt",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="valve1",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="valve2",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="valve3",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="valve4",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="workpermission",
            name="valve5",
            field=models.BooleanField(default=False),
        ),
    ]
