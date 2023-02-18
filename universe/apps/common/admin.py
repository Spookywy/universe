from apps.common.models import Distance, PlanetarySystem
from django.contrib import admin

admin.site.register(Distance)


@admin.register(PlanetarySystem)
class PlanetarySystemAdmin(admin.ModelAdmin):
    list_display = ("name", "star_name")

    def star_name(self, obj):
        return obj.star.name

    star_name.short_description = "Star"
