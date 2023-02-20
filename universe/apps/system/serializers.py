from rest_framework import serializers

from .models import PlanetarySystem


class PlanetarySystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PlanetarySystem
        fields = "__all__"
