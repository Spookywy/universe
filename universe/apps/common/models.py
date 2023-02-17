from django.db import models


class Distance(models.Model):
    UNIT_OF_MEASURE = [
        ("km", "Kilometre"),
        ("ly", "Light Year"),
    ]

    value = models.PositiveBigIntegerField(
        verbose_name="Value")
    unit_of_measure = models.CharField(max_length=255,
                                       choices=UNIT_OF_MEASURE, default="ly", verbose_name="Unit of measure")
