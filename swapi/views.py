from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.conf import settings

from keen.client import KeenClient

def index(request):

    keen = KeenClient(
        project_id=settings.KEEN_PROJECT_ID,
        write_key=settings.KEEN_WRITE_KEY,
        read_key=settings.KEEN_READ_KEY
    )
    hits = keen.count("detail_hit")
    return render_to_response('index.html',
        {
            "hits": hits
        }
    )


def documentation(request):
    return render_to_response("documentation.html")

def about(request):
    return render_to_response("about.html")
