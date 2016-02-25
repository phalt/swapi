from __future__ import unicode_literals

from rest_framework import serializers

from .models import (
    People,
    Planet,
    Film,
    Species,
    Vehicle,
    Starship,
)

class MetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
      abstract=True

    meta = serializers.SerializerMethodField()

    def get_meta(self, obj):
      return { "created": obj.created, "edited": obj.edited }

class PeopleSerializer(MetaSerializer):

    homeworld = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="planet-detail"
    )


    class Meta:
        model = People
        fields = (
            "name",
            "height",
            "mass",
            "hair_color",
            "skin_color",
            "eye_color",
            "birth_year",
            "gender",
            "homeworld",
            "films",
            "species",
            "vehicles",
            "starships",
            "created",
            "edited",
            "url",
            "meta"
        )



class PlanetSerializer(MetaSerializer):

    class Meta:
        model = Planet
        fields = (
            "name",
            "rotation_period",
            "orbital_period",
            "diameter",
            "climate",
            "gravity",
            "terrain",
            "surface_water",
            "population",
            "residents",
            "films",
            "created",
            "edited",
            "url",
            "meta"
        )


class FilmSerializer(MetaSerializer):

    class Meta:
        model = Film
        fields = (
            "title",
            "episode_id",
            "opening_crawl",
            "director",
            "producer",
	    "release_date",
            "characters",
            "planets",
            "starships",
            "vehicles",
            "species",
            "created",
            "edited",
            "url",
            "meta"
        )


class SpeciesSerializer(MetaSerializer):

    homeworld = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='planet-detail'
    )

    class Meta:
        model = Species
        fields = (
            "name",
            "classification",
            "designation",
            "average_height",
            "skin_colors",
            "hair_colors",
            "eye_colors",
            "average_lifespan",
            "homeworld",
            "language",
            "people",
            "films",
            "created",
            "edited",
            "url",
            "meta"
        )


class VehicleSerializer(MetaSerializer):

    pilots = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='people-detail'
    )

    class Meta:
        model = Vehicle
        fields = (
            "name",
            "model",
            "manufacturer",
            "cost_in_credits",
            "length",
            "max_atmosphering_speed",
            "crew",
            "passengers",
            "cargo_capacity",
            "consumables",
            "vehicle_class",
            "pilots",
            "films",
            "created",
            "edited",
            "url",
            "meta"
        )


class StarshipSerializer(MetaSerializer):

    pilots = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="people-detail"
    )

    class Meta:
        model = Starship
        fields = (
            "name",
            "model",
            "manufacturer",
            "cost_in_credits",
            "length",
            "max_atmosphering_speed",
            "crew",
            "passengers",
            "cargo_capacity",
            "consumables",
            "hyperdrive_rating",
            "MGLT",
            "starship_class",
            "pilots",
            "films",
            "created",
            "edited",
            "url",
            "meta"
        )

