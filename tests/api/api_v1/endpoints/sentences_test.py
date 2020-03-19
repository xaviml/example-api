import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.core import config
from app.main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "sentence, named_entities",
    [
        (
            "President Xi Jinping warned of the epidemic escalating outside the epicentre of Hubei province as more people travel and crowds gather across the country.",
            [
                {"entity": "Xi Jinping", "entity_type": "PERSON"},
                {"entity": "Hubei", "entity_type": "GPE"},
            ],
        ),
        (
            "Google LLC is an American multinational technology company",
            [
                {"entity": "Google LLC", "entity_type": "ORG"},
                {"entity": "American", "entity_type": "NORP"},
            ],
        ),
        ("This sentence does not have named entities", []),
    ],
)
def test_check(sentence, named_entities):
    response = client.post(
        config.API_V1 + "/sentence/process", json={"sentence": sentence}
    )
    assert response.status_code == 200
    assert response.json() == {"named_entities": named_entities}
