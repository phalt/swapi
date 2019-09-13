# SWAPI
## The Star Wars API

Source code for [swapi.co](https://swapi.co)

## Docker

To run Swapi on your Docker installation see the included Dockerfile. It is also available at Docker Hub <https://cloud.docker.com/repository/docker/svenwal/swapi/general>


```
docker run -d -p 8080:8080 svenwal/swapi
curl http://localhost:8080/api/people/1/
```

[![Circle CI](https://circleci.com/gh/phalt/swapi.svg?style=svg)](https://circleci.com/gh/phalt/swapi)

## Contributing

For contributing, please see CONTRIBUTING.md
