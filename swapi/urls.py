from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from .views import index, documentation, about, stats, stripe_donation

admin.autodiscover()

from rest_framework import routers

from resources import views

router = routers.DefaultRouter()

router.register(r"people", views.PeopleViewSet)
router.register(r"planets", views.PlanetViewSet)
router.register(r"films", views.FilmViewSet)
router.register(r"species", views.SpeciesViewSet)
router.register(r"vehicles", views.VehicleViewSet)
router.register(r"starships", views.StarshipViewSet)

urlpatterns = [
    path("", index),
    path("documentation", documentation),
    path("about", about),
    path("stats", stats),
    path("stripe/donation", stripe_donation),
    # url(r"^api/people/schema$", "resources.schemas.people"),
    # url(r"^api/planets/schema$", "resources.schemas.planets"),
    # url(r"^api/films/schema$", "resources.schemas.films"),
    # url(r"^api/species/schema$", "resources.schemas.species"),
    # url(r"^api/vehicles/schema$", "resources.schemas.vehicles"),
    # url(r"^api/starships/schema$", "resources.schemas.starships"),
    path("api/", include(router.urls)),
]
