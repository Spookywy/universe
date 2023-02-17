from apps.common.models import Distance
from django.db import models


class AstronomicalObject(models.Model):
    distanceFromEarth = models.ForeignKey(
        Distance, on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True
