from rest_framework import filters, viewsets

from .models import Galaxy, PlanetarySystem
from .serializers import GalaxySerializer, PlanetarySystemSerializer


class PlanetarySystemViewSet(viewsets.ModelViewSet):
    queryset = PlanetarySystem.objects.all().order_by("name")
    serializer_class = PlanetarySystemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "galaxy__name"]


class GalaxyViewSet(viewsets.ModelViewSet):
    queryset = Galaxy.objects.all().order_by("name")
    serializer_class = GalaxySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name",]
