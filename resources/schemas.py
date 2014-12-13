from __future__ import unicode_literals

from django.http import HttpResponse
from django.conf import settings

import json

import dkeen as keen


class JSONResponse():

    def __init__(self, resource):
        with open('resources/schemas/{0}.json'.format(resource)) as f:
            data = json.loads(f.read())
        self.data = data
        if not settings.DEBUG:
            keen.add_event(
                "schema_hit",
                {
                    "url": "/api/{0}/schema".format(resource),
                    "type": "schema",
                    "resource": "{0}".format(resource)

                }
            )

    @property
    def response(self):
        return HttpResponse(json.dumps(self.data), content_type="application/json")


def people(request):
    return JSONResponse('people').response


def planets(request):
    return JSONResponse('planets').response


def films(request):
    return JSONResponse('films').response


def species(request):
    return JSONResponse('species').response


def vehicles(request):
    return JSONResponse('vehicles').response


def starships(request):
    return JSONResponse('starships').response
