# Generated by Django 4.1.7 on 2023-02-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_add_mass_model"),
    ]

    operations = [
        migrations.AlterField(
            model_name="distance",
            name="unit_of_measure",
            field=models.CharField(
                choices=[("km", "Kilometre"), ("ly", "Light Year")],
                default="ly",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="distance",
            name="value",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="mass",
            name="unit_of_measure",
            field=models.CharField(
                choices=[("kg", "kilogram"), ("M☉", "solar mass")],
                default="kg",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="mass",
            name="value",
            field=models.CharField(max_length=255),
        ),
    ]