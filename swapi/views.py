from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required

import stripe

from resources.utils import get_resource_stats

DEFAULT_HITS = 50000


@cache_page(60 * 60)
def index(request):
    return render(request, 'index.html')


@cache_page(120 * 60)
def documentation(request):
    return render(request, "documentation.html")


@cache_page(120 * 60)
def about(request):
    data = get_resource_stats()
    return render(request, "about.html", data)


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


@login_required
def stats(request):
    data = {
        'keen_project_id': settings.KEEN_PROJECT_ID,
        'keen_read_key': settings.KEEN_READ_KEY
    }
    return render(request, 'stats.html', data)
