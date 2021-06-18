## What is this?

The Star Wars API is the world's first quantified and programmatically-formatted set of Star Wars data.

After hours of watching films and trawling through content online, we present to you all the **People, Films, Species, Starships, Vehicles and Planets** from Star Wars.

We've formatted this data in [**JSON**](https://json.org) and exposed it to you in a [**RESTish**](https://en.wikipedia.org/wiki/Representational_state_transfer) implementation that allows you to programmatically collect and measure the data.

[Check out the documentation to get started consuming swapi data](/documentation)

## What happened to swapi.co?
Unfortulately swapi.co is not maintained anymore, and the service is currently down. This is a branch of SWAPI that will be supported going forward.


## What can you use this for?

Comparing the data from Star Wars has never been easier. Here are some examples using the [Python helper library](/documentation#python)

*List the planets in order of size*:


    import swapi
    for planet in swapi.get_all("planets").order_by("diameter"):
        print(planet.name)


*View the people who have piloted more than one starship*:

    import swapi
    for people in swapi.get_all("people").iter():
        if len(people.starships) > 1:
            print(people.name)

*Discover if Jar Jar Binks ruined a film just by being in it*:

    import swapi
    pm = swapi.get_film(4)
    jj = swapi.get_person(36)
    for c in pm.get_characters().iter():
        if c.name == jj.name:
            print("Why George, why.")


## What are the features?

We're using [Django](https://djangoproject.com) and [Django REST Framework](https://django-rest-framework.org) to serve a [RESTish](https://en.wikipedia.org/wiki/REST) API to you.
The data is all formatted in [JSON](http://json.org) and we also support [JSON Schema](http://jsonschema.net) for programmatically understanding the attributes of each resource.

Seeing the release trailer for Episode VII also made me stupidly enthusiastic for Star Wars again.

## Who are you?

I am [Juriy Bura](https://github.com/juriy), Solution Architect and author of JavaScript game development book and online React courses.

## Original author?

This project was originally built and maintained by [Paul Hallett](http://phalt.co).

## Copyright and stuff?

Star Wars and all associated names are copyright Lucasfilm ltd.

This project is open source and carries a BSD licence.

All data has been freely collected from open sources such as [Wookiepedia](https://starwars.wikia.com).


## Contributors

SWAPI would not be possible without contributions from the following people:

- [Paul Hallett](https://phalt.co)
- [Owen Hallett](https://github.com/Videocard)
- [Carvilsi](https://github.com/carvilsi)
- [Andrea Stagi](https://github.com/astagi)
- [Juriy Bura](https://github.com/juriy)
