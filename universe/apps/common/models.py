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


class Mass(models.Model):
    UNIT_OF_MEASURE = [
        ("kg", "kilogram"),
        ("M☉", "solar mass"),
    ]

    value = models.CharField(max_length=255, verbose_name="Value")
    unit_of_measure = models.CharField(
        max_length=255,
        choices=UNIT_OF_MEASURE,
        default="kg",
        verbose_name="Unit of measure"
    )

    def __str__(self):
        return f"{self.value} {self.unit_of_measure}"
