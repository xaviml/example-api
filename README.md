[![azure-pipelines-build](https://img.shields.io/azure-devops/build/xaviml93/ControllerX/3/master.svg?style=for-the-badge)](https://dev.azure.com/xaviml93/ControllerX/_build/latest?definitionId=3&branchName=master)
[![azure-pipelines-coverage](https://img.shields.io/azure-devops/coverage/xaviml93/ControllerX/3/master.svg?style=for-the-badge)](https://dev.azure.com/xaviml93/ControllerX/_build/latest?definitionId=3&branchName=master)
[![last-release](https://img.shields.io/github/v/release/xaviml/example-api.svg?style=for-the-badge)](https://github.com/xaviml/controllerx/releases)

# Example API

This project was created for the purpose of an interview test. Its goal is to build an API endpoint that returns name entities given a sentence as an input.

## Dependencies

- FastAPI: Web framework to build APIs with Python
- spaCY: Library for NLP in Python
- pre-commit: It allows me to run some checks before a git commit is done
- commitizen: It gives a standard way to commit code and also allows me to version the code
- pytest: Used to run the tests
- Azure pipelines: Used to run a pipeline everytime there is a commit o a new tag is added for a new release with automated release notes

## Install

Install [pipenv](https://pipenv.kennethreitz.org/en/latest/install/#installing-pipenv) and then install dependencies:

```
pipenv install --dev
pipenv run pre-commit install
pipenv run spacy download en_core_web_sm
```

## Run

There are two ways to run the project, via Docker or through python virtual environment.

### With docker

If we want to run with Docker, we first need to build an image:

`docker build . -t example-api`

And then run an instance:

`docker run -i -d -p 8080:5000 example-api`

### Without docker

However, if we want to run without Docker, we can run directly with uvicorn:

```
pipenv run uvicorn --host 0.0.0.0 --port 5000 app.main:app
```

## Tests

Run this command to run tests with coverage:

`pipenv run pytest --cov=app`

## Formatting

Run the following command to format all the project:

`pipenv run pre-commit run --all-files`

## Deploying

By running `cz bump` it automatically detecs the version to bump - major, minor or patch. It follows [SemVer](https://semver.org/) standard. Then when pushing the code to GitHub, it needs to be done like this:

```
git push origin master --tags
```

It will then push the code and the Azure Pipeline will create the GitHub release if the pipeline passes.

### API and documentation

The API currently has 2 endpoints:

- `/api/v1/sentence/process`: It processess a sentence
- `/check`: It checks the system is running

Furthermore, FastAPI automatically generates the documentation for you, so when running you can access to `/docs` and you will be able to see in detail all the endpoints with its I/O.

For the sentence processing, I hace used `spacy`, a free open-source library for NLP in Python. [These](https://spacy.io/api/annotation#named-entities) are the named entity types that can be sent by the API.
