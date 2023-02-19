from django.urls import include, path
from rest_framework import routers

from .views import PlanetViewSet, StarViewSet

router = routers.DefaultRouter()
router.register(r"stars", StarViewSet)
router.register(r"planets", PlanetViewSet)

urlpatterns = [path("", include(router.urls))]
