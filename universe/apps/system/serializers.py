from rest_framework import serializers

from .models import Galaxy, PlanetarySystem


class PlanetarySystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanetarySystem
        fields = "__all__"


class GalaxySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Galaxy
        fields = "__all__"
