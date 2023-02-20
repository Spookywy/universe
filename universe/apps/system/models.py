from django.db import models


class Galaxy(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")

    def __str__(self):
        return self.name


class PlanetarySystem(models.Model):
    name = models.CharField(max_length=255, verbose_name="Name")
    galaxy = models.ForeignKey(
        Galaxy, on_delete=models.SET_NULL, null=True, related_name="planetary_systems")

    def __str__(self):
        return self.name
