from django.contrib import admin

from .models import PlanetarySystem


@admin.register(PlanetarySystem)
class PlanetarySystemAdmin(admin.ModelAdmin):
    list_display = ("name", "star_name")

    def star_name(self, obj):
        stars_set = obj.stars.all()
        if not stars_set.exists():
            return

        stars = []
        for star in obj.stars.all():
            stars.append(star.name)
        return "/".join(stars)

    star_name.short_description = "Stars"
