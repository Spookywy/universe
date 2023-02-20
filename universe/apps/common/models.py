from django.db import models


class Units(models.Model):
    value = models.CharField(max_length=255)
    unit_of_measure = models.CharField()

    def __str__(self):
        return f"{self.value} {self.unit_of_measure}"

    class Meta:
        abstract = True


class Distance(Units):
    UNIT_OF_MEASURE = [
        ("km", "Kilometre"),
        ("ly", "Light Year"),
    ]

    unit_of_measure = models.CharField(
        max_length=255,
        choices=UNIT_OF_MEASURE,
        default="ly",
    )


class Mass(Units):
    UNIT_OF_MEASURE = [
        ("kg", "kilogram"),
        ("M☉", "solar mass"),
    ]

    unit_of_measure = models.CharField(
        max_length=255,
        choices=UNIT_OF_MEASURE,
        default="kg",
    )
