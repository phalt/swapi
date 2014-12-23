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


def keen_hit(type, resource, request):
    if not settings.KEEN_DEBUG:
        ip = request.META['REMOTE_ADDR'] if request.META['REMOTE_ADDR'] else ''
        if request.META['HTTP_USER_AGENT']:
            user_agent = request.META['HTTP_USER_AGENT']
        else:
            user_agent = ''
        try:
            keen.add_event(
                "{0}_hit".format(type),
                {
                    "url": request.path,
                    "type": "{0}".format(type),
                    "resource": resource,
                    "ip_address": ip,
                    "user_agent": user_agent
                }
            )
        except:
            pass

class PeopleViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "people", request)
        return super(PeopleViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "people", request)
        return super(PeopleViewSet, self).list(request, *args, **kwargs)


class PlanetViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "planet", request)
        return super(PlanetViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "planet", request)
        return super(PlanetViewSet, self).list(request, *args, **kwargs)


class FilmViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Film.objects.all()
    serializer_class = FilmSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "film", request)
        return super(FilmViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "film", request)
        return super(FilmViewSet, self).list(request, *args, **kwargs)


class SpeciesViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "species", request)
        return super(SpeciesViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "species", request)
        return super(SpeciesViewSet, self).list(request, *args, **kwargs)


class VehicleViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "vehicle", request)
        return super(VehicleViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "vehicle", request)
        return super(VehicleViewSet, self).list(request, *args, **kwargs)


class StarshipViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Starship.objects.all()
    serializer_class = StarshipSerializer

    def retrieve(self, request, *args, **kwargs):
        keen_hit("detail", "starship", request)
        return super(StarshipViewSet, self).retrieve(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        keen_hit("list", "starship", request)
        return super(StarshipViewSet, self).list(request, *args, **kwargs)
