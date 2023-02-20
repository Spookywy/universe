from apps.common.serializers import MassSerializer
from rest_framework import serializers

from .models import Galaxy, PlanetarySystem


class PlanetarySystemSerializer(serializers.HyperlinkedModelSerializer):
    mass = MassSerializer()

    class Meta:
        model = PlanetarySystem
        fields = "__all__"


class GalaxySerializer(serializers.HyperlinkedModelSerializer):
    mass = MassSerializer()

    class Meta:
        model = Galaxy
        fields = "__all__"
