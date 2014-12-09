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
                "people_detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail"

                }
            )
        return super(PeopleViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "people_list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list"

                }
            )
        return super(PeopleViewSet, self).list(request, *args, **kwargs)


class PlanetViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

    def retrieve(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "planet_detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail"

                }
            )
        return super(PlanetViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "planet_list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list"

                }
            )
        return super(PlanetViewSet, self).list(request, *args, **kwargs)


class FilmViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def retrieve(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "film_detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail"

                }
            )
        return super(FilmViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "film_list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list"

                }
            )
        return super(FilmViewSet, self).list(request, *args, **kwargs)


class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

    def retrieve(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "species_detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail"

                }
            )
        return super(SpeciesViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "species_list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list"

                }
            )
        return super(SpeciesViewSet, self).list(request, *args, **kwargs)


class VehicleViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def retrieve(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "vehicle_detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail"

                }
            )
        return super(VehicleViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "vehicle_list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list"

                }
            )
        return super(VehicleViewSet, self).list(request, *args, **kwargs)


class StarshipViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer

    def retrieve(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "starshi_detail_hit",
                {
                    "url": request.get_full_path(),
                    "type": "detail"

                }
            )
        return super(StarshipViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        if not settings.DEBUG:
            keen.add_event(
                "starship_list_hit",
                {
                    "url": request.get_full_path(),
                    "type": "list"

                }
            )
        return super(StarshipViewSet, self).list(request, *args, **kwargs)
