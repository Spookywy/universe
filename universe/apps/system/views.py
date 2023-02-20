from rest_framework import viewsets

from .models import Galaxy, PlanetarySystem
from .serializers import GalaxySerializer, PlanetarySystemSerializer


class PlanetarySystemViewSet(viewsets.ModelViewSet):
    queryset = PlanetarySystem.objects.all().order_by("name")
    serializer_class = PlanetarySystemSerializer


class GalaxyViewSet(viewsets.ModelViewSet):
    queryset = Galaxy.objects.all().order_by("name")
    serializer_class = GalaxySerializer
