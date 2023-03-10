# Generated by Django 4.1.7 on 2023-02-22 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("astronomical_object", "0003_remove_unnecessary_verbose_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="planet",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="astronomicalObjects/"
            ),
        ),
        migrations.AddField(
            model_name="star",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="astronomicalObjects/"
            ),
        ),
    ]
