# Generated by Django 5.0.1 on 2024-08-14 06:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reliability", "0012_alter_reliability_componentcondition_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="reliability",
            name="record_date",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Record Date"
            ),
        ),
    ]
