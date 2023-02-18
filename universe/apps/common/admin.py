from apps.common.models import Distance, PlanetarySystem
from django.contrib import admin

admin.site.register(Distance)


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
