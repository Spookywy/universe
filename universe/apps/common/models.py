from django.db import models


class Distance(models.Model):
    UNIT_OF_MEASURE = [
        ("km", "Kilometre"),
        ("ly", "Light Year"),
    ]

    value = models.PositiveBigIntegerField(verbose_name="Value")
    unit_of_measure = models.CharField(
        max_length=255,
        choices=UNIT_OF_MEASURE,
        default="ly",
        verbose_name="Unit of measure",
    )


class PlanetarySystem(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    star = models.OneToOneField(
        "astronomical_object.Star",
        on_delete=models.CASCADE,
        related_name="planetary_system",
        verbose_name="Star",
    )
