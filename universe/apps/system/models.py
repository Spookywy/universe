from django.db import models


class System(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    mass = models.ForeignKey(
        "common.Mass",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Mass"
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Galaxy(System):
    pass


class PlanetarySystem(System):
    galaxy = models.ForeignKey(
        Galaxy,
        on_delete=models.SET_NULL,
        null=True,
        related_name="planetary_systems"
    )
