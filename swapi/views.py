from __future__ import unicode_literals

from django.shortcuts import response

def index(request):
    return response('index.html')
