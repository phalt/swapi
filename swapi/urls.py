from django.conf import settings
from django.conf.urls import include
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
    path("", index, name="homepage"),
    path("documentation", documentation, name="documentation"),
    path("about", about, name="about"),
    path("stats", stats, name="statistics"),
    path("stripe/donation", stripe_donation, name="donation"),
    path("api/people/schema", schemas.people),
    path("api/planets/schema", schemas.planets),
    path("api/films/schema", schemas.films),
    path("api/species/schema", schemas.species),
    path("api/vehicles/schema", schemas.vehicles),
    path("api/starships/schema", schemas.starships),
    path("api/", include(router.urls), name="api"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
