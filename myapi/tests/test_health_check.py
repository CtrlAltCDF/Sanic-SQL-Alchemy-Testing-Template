import pytest
from sanic import Sanic
from myapi import run

@pytest.fixture
def app() -> Sanic:
    return run(testing=True)

def test_confg(app: Sanic):
    assert app.config == 1
    assert app.config["APP_NAME"] == "go_fast" # this fails, fo some reason i get : Sanic app name "myapi" already in use.


def test_heath_check_endpoint(app: Sanic):
    request, response = app.test_client.get("/health_check")

    assert request.method.lower() == "get"
    assert response.json == {"health": "ok"}
    assert response.status == 200