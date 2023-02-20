from django.urls import include, path
from rest_framework import routers

from .views import GalaxyViewSet, PlanetarySystemViewSet

router = routers.DefaultRouter()
router.register(r"planetary-systems", PlanetarySystemViewSet)
router.register(r"galaxies", GalaxyViewSet)

urlpatterns = [path("", include(router.urls))]
