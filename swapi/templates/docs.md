
#Documentation
- - -
<a name="intro"></a>
###Introduction


Welcome to the swapi, the Star Wars API! This documentation should help you familiarise yourself with the resources available and how to consume them with HTTP requests. If you're after a native helper library then I suggest you scroll down and check out what's available. Read through the getting started section before you dive in. Most of your problems should be solved just by reading through it.

<a name="start"></a>
###Getting started


Let's make our first API request to the Star Wars API!

Open up a terminal and use [curl](http://curl.haxx.se) or [httpie](https://httpie.org) to make an API request for a resource. In the example below, we're trying to get the first planet, Tatooine:

    http swapi.co/api/planets/1/

We'll use [httpie](https://httpie.org) for our examples as it displays responses nicely and gives us a whole lot more useful information. If you don't want to download httpie, just use the *curl* command instead.

Here is the response we get:

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "climate": "Arid",
        "diameter": "10,465",
        "gravity": "1 standard",
        "name": "Tatooine",
        "orbital_period": "304",
        "population": "200,000",
        "residents": [
            "http://swapi.co/api/people/1/",
            "http://swapi.co/api/people/2/",
            ...
        ],
        "rotation_period": "23",
        "surface_water": "1%",
        "terrain": "Dessert",
        "url": "http://swapi.co/api/planets/1/"
    }

If your response looks slightly different don't panic. This is probably because more data has been added to swapi since we made this documenation.

<a name="base"></a>
###Base URL

The **Base URL** is the root URL for all of the API, if you ever make a request to swapi and you get back a **404 NOT FOUND** response then check the Base URL first.

The Base URL for swapi is:

    http://swapi.co/api/

The documentation below assumes you are prepending the Base URL to the endpoints in order to make requests.

<a name="rate"></a>
###Rate limiting

Swapi has rate limiting to prevent malicious abuse (as if anyone would abuse Star Wars data!) and to make sure our service can handle a potentially large amount of traffic. Rate limiting is done via IP address and is currently limited to 10,000 API request per day. This is enough to request all the data on the website at least ten times over. There should be no reason for hitting the rate limit.

<a name="auth"></a>
###Authentication

Swapi is a **completely open API**. No authenitcation is required to query and get data. This also means that we've limited what you can do to just **GET**-ing the data. If you find a mistake in the data, then [tweet the author](https://twitter.com/phalt_) or [email him](mailto:paulandrewhallett@gmail.com).

<a name="schema"></a>
###JSON Schema

All resources support [JSON Schema](https://jsonschema.net). Making a request to ```/api/<resource>/schema``` will give you the details of that resource. This will allow you to programmatically inspect the attributes of that resource and their types.

#Resources
- - -

<a name="root"></a>
###Root

The Root resource provides information on all avaiable resources within the API.

**Example request:**

    http http://swapi.co/api/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "films": "http://swapi.co/api/films/",
        "people": "http://swapi.co/api/people/",
        "planets": "http://swapi.co/api/planets/",
        "species": "http://swapi.co/api/species/",
        "starships": "http://swapi.co/api/starships/",
        "vehicles": "http://swapi.co/api/vehicles/"
    }

**Attributes:**

- ```films``` *string*
-- The URL root for Film resources
- ```people``` *string*
-- The URL root for People resources
- ```planets``` *string*
-- The URL root for Planet resources
- ```species``` *string*
-- The URL root for Species resources
- ```starships``` *string*
-- The URL root for Starships resources
- ```vehicles``` *string*
-- The URL root for Vehicles resources

<a name="people"></a>
###People

A People resource is an individual person or character within the Star Wars universe.

**Endpoints**

- ```/people/``` -- get all the people resources
- ```/people/:id/``` -- get a specific people resource
- ```/people/schema/``` -- view the JSON schema for this resource

**Example request:**

    http http://swapi.co/api/people/1/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "birth_year": "19 BBY",
        "eye_color": "Blue",
        "films": [
            "http://localhost:8000/api/films/1/",
            ...
        ],
        "gender": "Male",
        "hair_color": "Blond",
        "height": "1.72",
        "homeworld": "http://localhost:8000/api/planets/1/",
        "mass": "77",
        "name": "Luke Skywalker",
        "skin_color": "Fair",
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-10T13:52:43.172000Z",
        "species": [],
        "starships": [
            "http://localhost:8000/api/starships/12/",
            ...
        ],
        "url": "http://localhost:8000/api/people/1/",
        "vehicles": [
            "http://localhost:8000/api/vehicles/14/"
            ...
        ]
    }

**Attributes:**

- ```birth_year``` *string*
-- The birth year of the person, using the in-universe standard of **BBY** or **ABY** - Before the Battle of Yavin or After the Battle of Yavin. The Battle of Yavin is a battle that occurs at the end of Star Wars episode IV: A New Hope.
- ```eye_color``` *string*
-- The eye color of this person. Will be "unknown" if not known or "n/a" if the person does not have an eye.
- ```gender``` *string*
-- The gender of this person. Either "Male", "Female" or "unknown", "n/a" if the person does not have a gender.
- ```hair_color``` *string*
-- The hair color of this person. Will be "unknown" if not known or "n/a" if the person does not have hair.
- ```height``` *string*
-- The height of the person in meters.
- ```mass``` *string*
-- The mass of the person in kilograms.
- ```skin_color``` *string*
-- The skin color of this person.
- ```homeworld``` *string*
-- The URL of a planet resource, a planet that this person was born on or inhabits.
- ```films``` *array*
-- An array of film resource URLs that this person has been in.
- ```species``` *array*
-- An array of species resource URLs that this person belonds to.
- ```starships``` *array*
-- An array of starship resource URLs that this person has piloted.
- ```vehicles``` *array*
-- An array of vehicle resource URLs that this person has piloted.
- ```url``` *string*
-- the hypermedia URL of this resource.
- ```created``` *string*
-- the ISO 8601 date format of the time that this resource was created.
- ```edited``` *string*
-- the ISO 8601 date format of the time that this resource was edited.

<a name="films"></a>
###Film

A Film resource is an single film.

**Endpoints**

- ```/films/``` -- get all the film resources
- ```/films/:id/``` -- get a specific film resource
- ```/films/schema/``` -- view the JSON schema for this resource

**Example request:**

    http http://swapi.co/api/fims/1/

**Example response:**

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "characters": [
            "http://localhost:8000/api/people/1/",
            ...
        ],
        "created": "2014-12-10T14:23:31.880000Z",
        "director": "George Lucas",
        "edited": "2014-12-12T11:24:39.858000Z",
        "episode_id": 4,
        "opening_crawl": "It is a period of civil war.\n\nRebel spaceships, striking\n\nfrom a hidden base, have won\n\ntheir first victory against\n\nthe evil Galactic Empire.\n\n\n\nDuring the battle, Rebel\n\nspies managed to steal secret\r\nplans to the Empire's\n\nultimate weapon, the DEATH\n\nSTAR, an armored space\n\nstation with enough power\n\nto destroy an entire planet.\n\n\n\nPursued by the Empire's\n\nsinister agents, Princess\n\nLeia races home aboard her\n\nstarship, custodian of the\n\nstolen plans that can save her\n\npeople and restore\n\nfreedom to the galaxy....",
        "planets": [
            "http://localhost:8000/api/planets/1/",
            ...
        ],
        "producer": "Gary Kurtz, Rick McCallum",
        "species": [
            "http://localhost:8000/api/species/1/",
            ...
        ],
        "starships": [
            "http://localhost:8000/api/starships/2/",
            ...
        ],
        "title": "A New Hope",
        "url": "http://localhost:8000/api/films/1/",
        "vehicles": [
            "http://localhost:8000/api/vehicles/4/",
            ...
        ]
    }

**Attributes:**

- ```title``` *string*
-- The title of this film
- ```episode_id``` *integer*
-- The episode number of this film.
- ```opening_crawl``` *string*
-- The opening paragraphs at the beginning of this film.
- ```director``` *string*
-- The name of the director of this film.
- ```producer``` *string*
-- The name(s) of the producer(s) of this film. Comma seperated.
- ```species``` *array*
-- An array of species resource URLs that are in this film.
- ```starships``` *array*
-- An array of starship resource URLs that are in this film.
- ```vehicles``` *array*
-- An array of vehicle resource URLs that are in this film.
- ```characters``` *array*
-- An array of people resource URLs that are in this film.
- ```planets``` *array*
-- An array of planet resource URLs that are in this film.
- ```url``` *string*
-- the hypermedia URL of this resource.
- ```created``` *string*
-- the ISO 8601 date format of the time that this resource was created.
- ```edited``` *string*
-- the ISO 8601 date format of the time that this resource was edited.
