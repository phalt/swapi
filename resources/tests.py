from __future__ import unicode_literals

from django.test import TestCase

from .models import (
    People,
    Planet,
    Film,
    Species,
    Vehicle,
    Starship
)

from .renderers import WookieeRenderer
from datetime import datetime
from django.utils import timezone


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
        "films.json"
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

    def test_species_root(self):
        self.assertEqual(
            self.get_query("/api/species/").status_code, 200)

    def test_species_schema(self):
        self.assertEqual(
            self.get_query("/api/species/schema").status_code, 200)

    def get_timezone_aware_datetime(self, date_string):
        return timezone.make_aware(datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%fZ'), timezone.get_current_timezone())

    def test_people_detail(self):
        response = self.get_query("/api/people/1/")
        json_data = json.loads(response.content)
        person = People.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(person.name, json_data["name"])

    def test_people_meta_detail(self):
        response = self.get_query("/api/people/1/")
        json_data = json.loads(response.content)
        person = People.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(person.created, self.get_timezone_aware_datetime(json_data["meta"]["created"]))
        self.assertEqual(person.edited, self.get_timezone_aware_datetime(json_data["meta"]["edited"]))

    def test_planets_detail(self):
        response = self.get_query("/api/planets/1/")
        json_data = json.loads(response.content)
        planet = Planet.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(planet.name, json_data["name"])

    def test_planet_meta_detail(self):
        response = self.get_query("/api/planets/1/")
        json_data = json.loads(response.content)
        planet = Planet.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(planet.created, self.get_timezone_aware_datetime(json_data["meta"]["created"]))
        self.assertEqual(planet.edited, self.get_timezone_aware_datetime(json_data["meta"]["edited"]))

    def test_films_detail(self):
        response = self.get_query("/api/films/1/")
        json_data = json.loads(response.content)
        film = Film.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(film.title, json_data["title"])

    def test_film_meta_detail(self):
        response = self.get_query("/api/films/1/")
        json_data = json.loads(response.content)
        film = Film.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(film.created, self.get_timezone_aware_datetime(json_data["meta"]["created"]))
        self.assertEqual(film.edited, self.get_timezone_aware_datetime(json_data["meta"]["edited"]))

    def test_starships_detail(self):
        response = self.get_query("/api/starships/2/")
        json_data = json.loads(response.content)
        starship = Starship.objects.get(pk=2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(starship.name, json_data["name"])

    def test_starship_meta_detail(self):
        response = self.get_query("/api/starships/2/")
        json_data = json.loads(response.content)
        starship = Starship.objects.get(pk=2)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(starship.created, self.get_timezone_aware_datetime(json_data["meta"]["created"]))
        self.assertEqual(starship.edited, self.get_timezone_aware_datetime(json_data["meta"]["edited"]))

    def test_vehicles_detail(self):
        response = self.get_query("/api/vehicles/4/")
        json_data = json.loads(response.content)
        vehicle = Vehicle.objects.get(pk=4)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(vehicle.name, json_data["name"])

    def test_vehicle_meta_detail(self):
        response = self.get_query("/api/vehicles/4/")
        json_data = json.loads(response.content)
        vehicle = Vehicle.objects.get(pk=4)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(vehicle.created, self.get_timezone_aware_datetime(json_data["meta"]["created"]))
        self.assertEqual(vehicle.edited, self.get_timezone_aware_datetime(json_data["meta"]["edited"]))

    def test_species_detail(self):
        response = self.get_query("/api/species/1/")
        json_data = json.loads(response.content)
        specie = Species.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(specie.name, json_data["name"])

    def test_species_meta_detail(self):
        response = self.get_query("/api/species/1/")
        json_data = json.loads(response.content)
        species = Species.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(species.created, self.get_timezone_aware_datetime(json_data["meta"]["created"]))
        self.assertEqual(species.edited, self.get_timezone_aware_datetime(json_data["meta"]["edited"]))

    def test_etag(self):
        valid_etag = self.get_query("/api/")["ETag"]
        self.client.defaults['HTTP_IF_NONE_MATCH'] = valid_etag
        self.assertEqual(
            self.get_query("/api/").status_code, 304)

    def test_wookie_renderer(self):
        wookiee_renderer = WookieeRenderer()
        translated_data = wookiee_renderer.translate_to_wookie("swapi")
        self.assertEqual(translated_data, "cohraakah")
        translated_data = wookiee_renderer.translate_to_wookie("")
        self.assertEqual(translated_data, "")

    def test_wookie_format(self):
        wr = WookieeRenderer()
        response = self.get_query("/api/species/1/?format=wookiee")
        json_data = json.loads(response.content)
        specie = Species.objects.get(pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            wr.translate_to_wookie(specie.name),
            json_data[wr.translate_to_wookie("name")]
        )

