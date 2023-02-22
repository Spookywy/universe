from django.contrib import admin

from .models import Galaxy, PlanetarySystem


@admin.register(Galaxy)
class GalaxyAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(PlanetarySystem)
class PlanetarySystemAdmin(admin.ModelAdmin):
    list_display = ("name", "star_name")
    search_fields = ("name", "galaxy__name")

    def star_name(self, obj):
        stars_set = obj.stars.all()
        if not stars_set.exists():
            return

        stars = []
        for star in obj.stars.all():
            stars.append(star.name)
        return "/".join(stars)

    star_name.short_description = "Stars"
