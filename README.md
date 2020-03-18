# Example API

This project was created for the purpose of an interview test. Its goal is to build an API endpoint that returns name entities given a sentence as an input.

## Dependencies

- FastAPI: Web framework to build APIs with Python
- pre-commit: It allows me to run some checks before a git commit is done
- commitizen: It gives a standard way to commit code and also allows me to version the code
- pytest: Used to run the tests
- Azure pipelines: Used to run a pipeline everytime there is a commit o a new tag is added for a new release with automated release notes.

## Install

Install [pipenv](https://pipenv.kennethreitz.org/en/latest/install/#installing-pipenv) and then install dependencies:

```
pipenv install --dev
pipenv run pre-commit install
```

### Run

There are two ways to run the project, via Docker or through python virtual environment.

## With docker

If we want to run with Docker, we first need to build an image:

`docker build . -t example-api`

And then run an instance:

`docker run -i -d -p 8080:5000 example-api`

## Without docker

However, if we want to run without Docker, we can run directly with uvicorn:

```
pipenv run uvicorn --host 0.0.0.0 --port 5000 app.main:app
```

### Tests

python -m pytest --cov=app
