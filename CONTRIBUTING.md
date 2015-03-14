## Contributing

Make sure your contribution isn't already a planned feature or has already been fixed by checking the issues first.

1. Fork this project.

2. Find an issue to fix or create a new issue if you want to propose a feature. Generally speaking, everyone wants features. I'm only going to merge features that have 2 or more +1, otherwise this project will fill up with lots of randomly stuff.

3. Write your codez, make sure you add tests. Check out the "development" section below.

4. Submit a descriptive pull request that is *up to date with the master branch*.

5. We'll accept it and add it to production!


## Development

Once you have downloaded the project, look at the Makefile to see a list of useful shortcut commands.

In order to get started run:

```
make install
make build
make load_data
```

To run the server locally run:

```
make serve
```

If you add new data then you can dump it out using the following command:

```
make dumpdata
```

To run tests:

```
make test
```

*NOTE:* pull requests will not be accepted if they do not pass tests or have no new tests for new features.


## File structure

- resources

All API resource models, serializers and schemas are found here.

- swapi

All Django configuration, templates and static files are found here.
