# Generated by Django 4.2.6 on 2024-04-18 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_plant"),
        ("ceList", "0009_rename_celist_id_celist_celistno"),
        ("junctionTable", "0009_remove_eventyearppm_companyname_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="eventyearppm",
            name="companyName",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eventYearPPM_companyName",
                to="accounts.companyname",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="equipment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eventYearPPM_equipment",
                to="ceList.equipment",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="machine",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eventYearPPM_machine",
                to="ceList.machine",
            ),
        ),
        migrations.AddField(
            model_name="eventyearppm",
            name="plant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eventYearPPM_plant",
                to="accounts.plant",
            ),
        ),
        migrations.AlterField(
            model_name="eventyearppm",
            name="companyCode",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="eventYearPPM_companyCode",
                to="accounts.companycode",
            ),
        ),
    ]
