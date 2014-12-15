
#Documentation
- - -
<a name="intro"></a>
###Introduction


Welcome to the swapi, the Star Wars API! This documentation should help you familiarise yourself with the resources available and how to consume them with HTTP requests. If you're after a native helper library then I suggest you scroll down and check out what's available. Read through the getting started section before you dive in. Most of your problems should be solved jusy by reading through that.

<a name="start"></a>
###Getting started


Let's get our first API request to the Star Wars API out of the way. Open up a terminal and use [curl](http://curl.haxx.se) or [httpie](https://httpie.org) to make an API request a resource. In the example below, we're trying to get the first planet, Tatooine:

    http swapi.co/api/planets/1/

We'll use [httpie](https://httpie.org) for our examples as it displays responses nicely and gives us a whole lot more useful information.

Here is the response we get:

    HTTP/1.0 200 OK
    Content-Type: application/json
    {
        "climate": "Arid",
        "diameter": "10,465",
        "gravity": "1 standard",
        "name": "Tatooine",
        "orbital_period": "304 days",
        "population": "80,000-200,000",
        "residents": [
            "http://swapi.co/api/people/1/",
            "http://swapi.co/api/people/2/",
            ...
        ],
        "rotation_period": "23 hours",
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

<a name="rate"></a>
###Rate limiting

Swapi has rate limiting to prevent malicious abuse (as if anyone would abuse Star Wars data!) and to make sure our service can handle a potentially large amount of traffic. Rate limiting is done via IP address and is currently limited to 10,000 API request per day. Which is enough to request the data on the website at least ten times over. There should be no reason for hitting the rate limit.

<a name="auth"></a>
###Authentication

Swapi is a **completely open API**. No authenitcation is required to query and get data. This also means that we've limited what you can do to just **GET**-ing the data. If you find a mistake in the code, then [tweet the author](https://twitter.com/phalt_) or [email him](mailto:paulandrewhallett@gmail.com).


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
-- The URL root for ```Film``` resources
- ```people``` *string*
-- The URL root for ```People``` resources
- ```planets``` *string*
-- The URL root for ```People``` resources
- ```species``` *string*
-- The URL root for ```Species``` resources
- ```starships``` *string*
-- The URL root for ```Starships``` resources
- ```vehicles``` *string*
-- The URL root for ```Vehicles``` resources

<a name="people"></a>
###People

A ```People``` resource is an individual person or character within the Star Wars universe.

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
        "height": "1.72 m",
        "homeworld": "http://localhost:8000/api/planets/1/",
        "mass": "77 Kg",
        "name": "Luke Skywalker",
        "skin_color": "Fair",
        "species": [],
        "starships": [
            "http://localhost:8000/api/starships/12/",
            ...
        ],
        "url": "http://localhost:8000/api/people/1/",
        "vehicles": [
            "http://localhost:8000/api/vehicles/14/"
        ]
    }

**Attributes:**

- ```birth_year``` *string*
-- The birth year of the person, using the in-universe standard of **BBY** or **ABY** - Before the Battle of Yavin or After the Battle of Yavin. The Battle of Yavin is a battle that occurs at the end of Star Wars episode IV: A New Hope.
- ```eye_color``` *string*
-- The eye color of this person. Will be "unknown" if not known or "n/a" if the person does not have an eye.
- ```gender``` *string*
-- the gender of this person. Either "Male", "Female" or "unknown", "n/a" if the person does not have a gender.
- ```hair_color``` *string*
-- the hair color of this person. Will be "unknown" if not known or "n/a" if the person does not have hair.
- ```height``` *string*
-- the height of the person in meters.
- ```mass``` *string*
-- the mass of the person in kilograms.
- ```skin_color``` *string*
-- the skin color of this person.
- ```url``` *string*
-- the hypermedia URL of this resource.
- ```films``` *array*
-- An array of film resource URLs that this person has been in.
- ```species``` *array*
-- An array of species resource URLs that this person belonds to.
- ```starships``` *array*
-- An array of starship resource URLs that this person has piloted.
- ```vehicles``` *array*
-- An array of vehicle resource URLs that this person has piloted.
