from __future__ import unicode_literals

from django.test import TestCase

from .models import (
    People,
    Planet,
    Film,
    Species,
    Vehicle,
    Starship,
    Faction
)

import json

class TestAllEndpoints(TestCase):
    """ Test ALL the endpoints """
    fixtures = [
        "planets.json",
        "people.json",
        "species.json",
        "starships.json",
        "vehicles.json",
        "transport.json",
        "films.json",
        "factions.json"
    ]

    def get_query(self, url):
        return self.client.get(url)

    def test_api_root(self):
        self.assertEqual(
            self.get_query("/api/").status_code, 200)

    def test_people_root(self):
        self.assertEqual(
            self.get_query("/api/people/").status_code, 200)

    def test_people_schema(self):
        self.assertEqual(
            self.get_query("/api/people/schema").status_code, 200)

    def test_planets_root(self):
        self.assertEqual(
            self.get_query("/api/planets/").status_code, 200)

    def test_planets_schema(self):
        self.assertEqual(
            self.get_query("/api/planets/schema").status_code, 200)

    def test_films_root(self):
        self.assertEqual(
            self.get_query("/api/films/").status_code, 200)

    def test_films_schema(self):
        self.assertEqual(
            self.get_query("/api/films/schema").status_code, 200)

    def test_starships_root(self):
        self.assertEqual(
            self.get_query("/api/starships/").status_code, 200)

    def test_starship_schema(self):
        self.assertEqual(
            self.get_query("/api/starships/schema").status_code, 200)

    def test_vehicles_root(self):
        self.assertEqual(
            self.get_query("/api/vehicles/").status_code, 200)

    def test_vehicle_schema(self):
        self.assertEqual(
            self.get_query("/api/vehicles/schema").status_code, 200)

    def test_faction_schema(self):
        self.assertEqual(
            self.get_query("/api/factions/schema").status_code, 200)

    def test_species_root(self):
        self.assertEqual(
            self.get_query("/api/species/").status_code, 200)

    def test_species_schema(self):
        self.assertEqual(
            self.get_query("/api/species/schema").status_code, 200)

    def test_people_detail(self):
        response = self.get_query("/api/people/1/")
        json_data = json.loads(response.content)
        person = People.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(person.name, json_data["name"])

    def test_planets_detail(self):
        response = self.get_query("/api/planets/1/")
        json_data = json.loads(response.content)
        planet = Planet.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(planet.name, json_data["name"])

    def test_films_detail(self):
        response = self.get_query("/api/films/1/")
        json_data = json.loads(response.content)
        film = Film.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(film.title, json_data["title"])

    def test_starships_detail(self):
        response = self.get_query("/api/starships/2/")
        json_data = json.loads(response.content)
        starship = Starship.objects.get(pk=2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(starship.name, json_data["name"])

    def test_vehicles_detail(self):
        response = self.get_query("/api/vehicles/4/")
        json_data = json.loads(response.content)
        vehicle = Vehicle.objects.get(pk=4)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(vehicle.name, json_data["name"])

    def test_species_detail(self):
        response = self.get_query("/api/species/1/")
        json_data = json.loads(response.content)
        specie = Species.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(specie.name, json_data["name"])

    def test_factions_detail(self):
        response = self.get_query("/api/factions/1/")
        json_data = json.loads(response.content)
        fac = Faction.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(fac.name, json_data["name"])
