from django.db import models


class Distance(models.Model):
    UNIT_OF_MEASURE = [
        ("km", "Kilometre"),
        ("ly", "Light Year"),
    ]

    value = models.CharField(max_length=255, verbose_name="Value")
    unit_of_measure = models.CharField(
        max_length=255,
        choices=UNIT_OF_MEASURE,
        default="ly",
        verbose_name="Unit of measure",
    )

    def __str__(self):
        return f"{self.value} {self.unit_of_measure}"


class PlanetarySystem(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")

    def __str__(self):
        return self.name
