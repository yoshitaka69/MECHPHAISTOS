# Generated by Django 5.0.1 on 2024-03-05 18:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                ("freeUser", models.BooleanField(default=False)),
                ("lightUser", models.BooleanField(default=False)),
                ("middleUser", models.BooleanField(default=False)),
                ("specialUser", models.BooleanField(default=False)),
                ("premiumUser", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Company",
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
                    "companyCode",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="companyCode",
                    ),
                ),
                (
                    "companyListNo",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="companyListNo",
                    ),
                ),
                (
                    "companyName",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="companyName",
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="country"
                    ),
                ),
                (
                    "zipCode",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="zipCode"
                    ),
                ),
                ("createdDay", models.DateTimeField(auto_now_add=True)),
                ("updateDay", models.DateTimeField(auto_now_add=True)),
                (
                    "payment",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.payment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "firstName",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="firstName"
                    ),
                ),
                (
                    "familyName",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="familyName"
                    ),
                ),
                (
                    "userName",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="userName"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "phoneNumber",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="phoneNumber",
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                (
                    "createdDay",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="createdDay"
                    ),
                ),
                (
                    "updateDay",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="updateDay"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
                (
                    "company",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.company",
                    ),
                ),
                (
                    "payment",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="accounts.payment",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]