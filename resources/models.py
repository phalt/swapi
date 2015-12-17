from __future__ import unicode_literals

from django.db import models


class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)

    edited = models.DateTimeField(auto_now=True)


class EditableModel(models.Model):
    """
    A model with a boolean that determins the read/write state of the model
    """

    editable = models.NullBooleanField()


class Planet(DateTimeModel):
    """ A planet i.e. Tatooine """

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)

    rotation_period = models.CharField(max_length=40)

    orbital_period = models.CharField(max_length=40)

    diameter = models.CharField(max_length=40)

    climate = models.CharField(max_length=40)

    gravity = models.CharField(max_length=40)

    terrain = models.CharField(max_length=40)

    surface_water = models.CharField(max_length=40)

    population = models.CharField(max_length=40)


class People(DateTimeModel):
    """ A person i.e. - Luke Skywalker """

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=100)

    height = models.CharField(max_length=10, blank=True)

    mass = models.CharField(max_length=10, blank=True)

    hair_color = models.CharField(max_length=20, blank=True)

    skin_color = models.CharField(max_length=20, blank=True)

    eye_color = models.CharField(max_length=20, blank=True)

    birth_year = models.CharField(max_length=10, blank=True)

    gender = models.CharField(max_length=40, blank=True)

    homeworld = models.ForeignKey(Planet, related_name="residents")


class Transport(DateTimeModel):

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=40)

    model = models.CharField(max_length=40)

    manufacturer = models.CharField(max_length=80)

    cost_in_credits = models.CharField(max_length=40)

    length = models.CharField(max_length=40)

    max_atmosphering_speed = models.CharField(max_length=40)

    crew = models.CharField(max_length=40)

    passengers = models.CharField(max_length=40)

    cargo_capacity = models.CharField(max_length=40)

    consumables = models.CharField(max_length=40)


class Starship(Transport):
    """ A starship is a transport with a hypderdrive """

    hyperdrive_rating = models.CharField(max_length=40)

    MGLT = models.CharField(max_length=40)

    starship_class = models.CharField(max_length=40)

    pilots = models.ManyToManyField(
        People,
        related_name="starships",
        blank=True
    )


class Vehicle(Transport):
    """ A vehicle is anything without hyperdrive capability """

    vehicle_class = models.CharField(max_length=40)

    pilots = models.ManyToManyField(
        People,
        related_name="vehicles",
        blank=True
    )


class Species(DateTimeModel):
    "A species is a type of alien or person"

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=40)

    classification = models.CharField(max_length=40)

    designation = models.CharField(max_length=40)

    average_height = models.CharField(max_length=40)

    skin_colors = models.CharField(max_length=200)

    hair_colors = models.CharField(max_length=200)

    eye_colors = models.CharField(max_length=200)

    average_lifespan = models.CharField(max_length=40)

    homeworld = models.ForeignKey(Planet, blank=True, null=True)

    language = models.CharField(max_length=40)

    people = models.ManyToManyField(People, related_name="species")


class Film(DateTimeModel):
    """ A film i.e. The Empire Strikes Back (which is also the best film) """

    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=100)

    episode_id = models.IntegerField()

    opening_crawl = models.TextField(max_length=1000)

    director = models.CharField(max_length=100)

    producer = models.CharField(max_length=100)

    release_date = models.DateField()

    characters = models.ManyToManyField(
        People,
        related_name="films",
        blank=True
    )

    planets = models.ManyToManyField(
        Planet,
        related_name="films",
        blank=True
    )

    starships = models.ManyToManyField(
        Starship,
        related_name="films",
        blank=True
    )

    vehicles = models.ManyToManyField(
        Vehicle,
        related_name="films",
        blank=True
    )

    species = models.ManyToManyField(
        Species,
        related_name="films",
        blank=True
    )

