FROM python:3.8.2-slim-buster
LABEL maintainer="xaviml"

RUN apt-get update && apt-get install -y python3-dev build-essential
RUN apt-get install pipenv -y

RUN mkdir -p /usr/src/example-api
WORKDIR /usr/src/example-api

COPY . .

RUN pipenv install
RUN pipenv run spacy download en_core_web_sm

EXPOSE 5000

CMD ["pipenv","run","uvicorn", "--host", "0.0.0.0", "--port", "5000", "app.main:app"]
