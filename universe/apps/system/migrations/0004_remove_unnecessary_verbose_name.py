# Generated by Django 4.1.7 on 2023-02-20 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0003_remove_unnecessary_verbose_name"),
        ("system", "0003_add_mass_field_to_system"),
    ]

    operations = [
        migrations.AlterField(
            model_name="galaxy",
            name="mass",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="common.mass",
            ),
        ),
        migrations.AlterField(
            model_name="galaxy",
            name="name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="planetarysystem",
            name="mass",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="common.mass",
            ),
        ),
        migrations.AlterField(
            model_name="planetarysystem",
            name="name",
            field=models.CharField(max_length=255),
        ),
    ]