# Generated by Django 5.0.1 on 2024-03-16 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("taskList", "0005_alter_tasklist_laborcostofpm"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tasklist",
            name="equipment",
        ),
        migrations.RemoveField(
            model_name="tasklist",
            name="machineName",
        ),
        migrations.RemoveField(
            model_name="tasklist",
            name="plant",
        ),
        migrations.RemoveField(
            model_name="tasklist",
            name="typeOfPM",
        ),
    ]