from django.urls import include, path
from rest_framework import routers

from .views import PlanetarySystemViewSet

router = routers.DefaultRouter()
router.register(r"planetary-systems", PlanetarySystemViewSet)

urlpatterns = [path("", include(router.urls))]
