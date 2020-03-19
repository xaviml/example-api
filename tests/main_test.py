from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_check():
    response = client.get("/check")
    assert response.status_code == 200
    assert response.json() == {"message": "example-api is alive!"}
