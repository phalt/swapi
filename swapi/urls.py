from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers

from resources import schemas
from resources import views
from .views import index, documentation, about, stats, stripe_donation

router = routers.DefaultRouter()

router.register(r"people", views.PeopleViewSet)
router.register(r"planets", views.PlanetViewSet)
router.register(r"films", views.FilmViewSet)
router.register(r"species", views.SpeciesViewSet)
router.register(r"vehicles", views.VehicleViewSet)
router.register(r"starships", views.StarshipViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path("documentation", documentation),
    path("about", about),
    path("stats", stats),
    path("stripe/donation", stripe_donation),
    path("api/people/schema", schemas.people),
    path("api/planets/schema", schemas.planets),
    path("api/films/schema", schemas.films),
    path("api/species/schema", schemas.species),
    path("api/vehicles/schema", schemas.vehicles),
    path("api/starships/schema", schemas.starships),
    url(r"^api/", include(router.urls)),
]
