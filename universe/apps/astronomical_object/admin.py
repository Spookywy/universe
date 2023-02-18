from apps.astronomical_object.models import Planet, Star
from django.contrib import admin


@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ("name", "planetary_system_name")

    def planetary_system_name(self, obj):
        if obj.planetary_system:
            return obj.planetary_system.name
        return

    planetary_system_name.short_description = "Planetary system"


@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ("name", "planetary_system_name")

    def planetary_system_name(self, obj):
        if obj.planetary_system:
            return obj.planetary_system.name
        return

    planetary_system_name.short_description = "Planetary system"
