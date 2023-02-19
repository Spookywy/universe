from rest_framework import viewsets

from .models import Planet, Star
from .serializers import PlanetSerializer, StarSerializer


class StarViewSet(viewsets.ModelViewSet):
    queryset = Star.objects.all().order_by("name")
    serializer_class = StarSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    queryset = Planet.objects.all().order_by("name")
    serializer_class = PlanetSerializer
