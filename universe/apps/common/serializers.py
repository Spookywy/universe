from rest_framework import serializers

from .models import Distance, PlanetarySystem


class DistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = "__all__"


class PlanetarySystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanetarySystem
        fields = "__all__"
