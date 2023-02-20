from rest_framework import serializers

from .models import Distance, Mass


class DistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distance
        fields = ("value", "unit_of_measure")


class MassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mass
        fields = ("value", "unit_of_measure")
