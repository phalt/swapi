from __future__ import unicode_literals

from .models import (
    People,
    Planet,
    Film,
    Species,
    Vehicle,
    Starship,
)

def get_resource_stats():
    return {
        'people': People.objects.count(),
        'planets': Planet.objects.count(),
        'films': Film.objects.count(),
        'species': Species.objects.count(),
        'vehicles': Vehicle.objects.count(),
        'starships': Starship.objects.count()
    }
