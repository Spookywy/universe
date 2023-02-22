from rest_framework import filters, viewsets

from .models import Planet, Star
from .serializers import PlanetSerializer, StarSerializer


class AstronomicalObjectViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "planetary_system__name"]

    class Meta:
        abstract = True


class StarViewSet(AstronomicalObjectViewSet):
    queryset = Star.objects.all().order_by("name")
    serializer_class = StarSerializer


class PlanetViewSet(AstronomicalObjectViewSet):
    queryset = Planet.objects.all().order_by("name")
    serializer_class = PlanetSerializer
