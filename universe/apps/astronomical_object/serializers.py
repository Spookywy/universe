from apps.common.serializers import DistanceSerializer
from rest_framework import serializers

from .models import Planet, Star


class StarSerializer(serializers.HyperlinkedModelSerializer):
    distance_from_earth = DistanceSerializer()

    class Meta:
        model = Star
        fields = "__all__"


class PlanetSerializer(serializers.HyperlinkedModelSerializer):
    distance_from_earth = DistanceSerializer()

    class Meta:
        model = Planet
        fields = "__all__"
