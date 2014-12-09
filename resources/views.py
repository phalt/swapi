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


class PeopleViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def retrieve(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail",
                    "resource": "people"

                }
            )
        return super(PeopleViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list",
                    "resource": "people"

                }
            )
        return super(PeopleViewSet, self).list(request, *args, **kwargs)


class PlanetViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

    def retrieve(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail",
                    "resource": "planet"

                }
            )
        return super(PlanetViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list",
                    "resource": "planet"

                }
            )
        return super(PlanetViewSet, self).list(request, *args, **kwargs)


class FilmViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def retrieve(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail",
                    "resource": "film"

                }
            )
        return super(FilmViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list",
                    "resource": "film"

                }
            )
        return super(FilmViewSet, self).list(request, *args, **kwargs)


class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

    def retrieve(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail",
                    "resource": "species"

                }
            )
        return super(SpeciesViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list",
                    "resource": "species"

                }
            )
        return super(SpeciesViewSet, self).list(request, *args, **kwargs)


class VehicleViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def retrieve(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail",
                    "resource": "vehicle"

                }
            )
        return super(VehicleViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list",
                    "resource": "vehicle"

                }
            )
        return super(VehicleViewSet, self).list(request, *args, **kwargs)


class StarshipViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer

    def retrieve(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail",
                    "resource": "starship"

                }
            )
        return super(StarshipViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list",
                    "resource": "starship"

                }
            )
        return super(StarshipViewSet, self).list(request, *args, **kwargs)
