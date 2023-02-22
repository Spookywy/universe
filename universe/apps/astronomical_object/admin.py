from django.contrib import admin

from .models import Planet, Star


@admin.register(Planet, Star)
class AstronomicalObjectAdmin(admin.ModelAdmin):
    list_display = ("name", "planetary_system_name")
    search_fields = ("name", "planetary_system__name")

    def planetary_system_name(self, obj):
        if obj.planetary_system:
            return obj.planetary_system.name
        return

    planetary_system_name.short_description = "Planetary system"
