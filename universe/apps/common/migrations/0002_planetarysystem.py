# Generated by Django 4.1.7 on 2023-02-18 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("astronomical_object", "0001_initial"),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlanetarySystem",
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
                ("name", models.CharField(max_length=255, verbose_name="Name")),
                (
                    "star",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="astronomical_object.star",
                        verbose_name="Star",
                    ),
                ),
            ],
        ),
    ]