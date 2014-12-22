from __future__ import unicode_literals

from django.conf import settings

from rest_framework import viewsets

from .models import (
    People,
    Planet,
    Film,
    Species,
    Vehicle,
    Starship
)

from .serializers import (
    PeopleSerializer,
    PlanetSerializer,
    FilmSerializer,
    SpeciesSerializer,
    VehicleSerializer,
    StarshipSerializer
)

import dkeen as keen


def keen_hit(type, resource, url):
    if not settings.KEEN_DEBUG:
        keen.add_event(
            "{0}_hit".format(type),
            {
                "url": url,
                "type": "{0}".format(type),
                "resource": "resource"

            }
        )

class PeopleViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "people", request.get_full_path())
        return super(PeopleViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "people", request.get_full_path())
        return super(PeopleViewSet, self).list(request, *args, **kwargs)


class PlanetViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "planet", request.get_full_path())
        return super(PlanetViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "planet", request.get_full_path())
        return super(PlanetViewSet, self).list(request, *args, **kwargs)


class FilmViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "film", request.get_full_path())
        return super(FilmViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "film", request.get_full_path())
        return super(FilmViewSet, self).list(request, *args, **kwargs)


class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "species", request.get_full_path())
        return super(SpeciesViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "species", request.get_full_path())
        return super(SpeciesViewSet, self).list(request, *args, **kwargs)


class VehicleViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "vehicle", request.get_full_path())
        return super(VehicleViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "vehicle", request.get_full_path())
        return super(VehicleViewSet, self).list(request, *args, **kwargs)


class StarshipViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "starship", request.get_full_path())
        return super(StarshipViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "starship", request.get_full_path())
        return super(StarshipViewSet, self).list(request, *args, **kwargs)
