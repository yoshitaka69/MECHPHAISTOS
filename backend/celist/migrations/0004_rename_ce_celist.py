# Generated by Django 5.0.1 on 2024-03-07 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        ("ceList", "0003_alter_ce_bomno_alter_ce_tasklistno"),
        ("repairingCost", "0001_initial"),
        ("spareParts", "0001_initial"),
        ("sustainability", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Ce",
            new_name="CeList",
        ),
    ]