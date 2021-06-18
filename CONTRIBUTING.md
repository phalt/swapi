## Contributing

Make sure your contribution isn't already a planned feature or has already 
been fixed by checking the issues first.

1. Fork this project.

2. Find an issue to fix or create a new issue if you want to propose a feature. For 
   the new features - check out on GitHub issues first before starting to code it.
   
3. **No changes in the current API** are accepted. Even backward-compatible ones. 
   The only exception is extending database and fixing data issues. These are OK. For 
   all other changes - please submit a request and we'll review the feature for v2 of API. 
   Current version will remain the same for the sake of compatibility with all the 
   example code that API enthusiasts created.

## Development

An application was originally built with Python 2.7 and Django 1.x. This stack is outdated hence
continuing with this code base is not adviced. The next version of SWAPI will likely be 
cloud native and serverless. 

If you insist, best use Docker for building and running the project (Dockerfile is included 
in the root folder)

```shell
docker build -t myswapi .
docker run -p 8000:8000 myswapi
```

The same image is available as `juriy/swapi` from DockerHub.

# Django commands

The commands below are already executed in Docker image, if you need to work with Django
directly or from inside the docker image, the following commands may be useful

```shell
# run DB migrations
python manage.py migrate

# load data from fixtures
make load_data

# run the server
python manage.py runserver 0.0.0.0:8000
```

If you add new data then you can dump it out using the following command:

```
make dumpdata
```

To run tests:

```
make test
```

## File structure

### /resources
All API resource models, serializers and schemas are found here.

### /swapi
All Django configuration, templates and static files are found here.
