from rest_framework import viewsets

from .models import PlanetarySystem
from .serializers import PlanetarySystemSerializer


class PlanetarySystemViewSet(viewsets.ModelViewSet):
    queryset = PlanetarySystem.objects.all().order_by("name")
    serializer_class = PlanetarySystemSerializer
