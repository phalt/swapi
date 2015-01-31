from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    People,
    Planet,
    Film,
    Starship,
    Vehicle,
    Species,
    Faction

)

classes = [People, Planet, Film, Starship, Vehicle, Species, Faction]

for c in classes:
    admin.site.register(c)
