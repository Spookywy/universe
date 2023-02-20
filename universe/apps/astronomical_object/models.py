from django.db import models


class AstronomicalObject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    distance_from_earth = models.ForeignKey(
        "common.Distance",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Distance from Earth",
    )
    radius = models.PositiveIntegerField(verbose_name="Radius (km)")
    surface_temperature = models.BigIntegerField(
        verbose_name="Temperature of the surface (Kelvin)"
    )

    class Meta:
        abstract = True


class Star(AstronomicalObject):
    CLASSES = [
        ("o", "O"),
        ("b", "B"),
        ("a", "A"),
        ("f", "F"),
        ("g", "G"),
        ("k", "K"),
        ("m", "M"),
    ]

    classification = models.CharField(
        max_length=255, choices=CLASSES, verbose_name="Classification"
    )
    planetary_system = models.ForeignKey(
        "system.PlanetarySystem",
        on_delete=models.SET_NULL,
        null=True,
        related_name="stars",
    )

    def __str__(self):
        return self.name


class Planet(AstronomicalObject):
    planetary_system = models.ForeignKey(
        "system.PlanetarySystem",
        on_delete=models.SET_NULL,
        null=True,
        related_name="planets",
    )
