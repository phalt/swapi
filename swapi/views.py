from __future__ import unicode_literals

from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from keen.client import KeenClient
import stripe

from resources.utils import get_resource_stats

def index(request):

    keen = KeenClient(
        project_id=settings.KEEN_PROJECT_ID,
        write_key=settings.KEEN_WRITE_KEY,
        read_key=settings.KEEN_READ_KEY
    )
    hits = keen.count("detail_hit")
    stripe_key = settings.STRIPE_KEYS['publishable']
    return render_to_response('index.html',
        {
            "hits": hits,
            "stripe_key": stripe_key
        }
    )


def documentation(request):
    return render_to_response("documentation.html")


def about(request):
    stripe_key = settings.STRIPE_KEYS['publishable']

    data = get_resource_stats()
    data['stripe_key'] = stripe_key
    return render_to_response(
        "about.html",
        data
    )

@csrf_exempt
def stripe_donation(request):
    if request.method == 'POST':
        # Amount in cents
        amount = 1000

        stripe.api_key = settings.STRIPE_KEYS['secret']

        customer = stripe.Customer.create(
            email=request.POST.get('stripeEmail', ''),
            card=request.POST.get('stripeToken', '')
        )

        try:
            stripe.Charge.create(
                customer=customer.id,
                amount=amount,
                currency='usd',
                description='SWAPI donation'
            )
        except:
            pass

        return redirect('/')
    return redirect('/')
