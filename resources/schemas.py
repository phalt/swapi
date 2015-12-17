from __future__ import unicode_literals

from django.http import HttpResponse

import json


class JSONResponse():

    def __init__(self, resource):
        with open('resources/schemas/{0}.json'.format(resource)) as f:
            data = json.loads(f.read())
        self.data = data

    @property
    def response(self):
        return HttpResponse(
            json.dumps(self.data),
            content_type="application/json"
        )


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
