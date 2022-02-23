import pytest
from sanic import Sanic
from myapi import app as myapi_app

@pytest.fixture(scope="function")
def app() -> Sanic:
    return myapi_app("test")

def test_confg(app: Sanic):
    assert app.config["APP_NAME"] == 'myapi_test'
    assert app.config["SQLALCHEMY_URL"] == 'sqlite+aiosqlite:///:memory:'


def test_heath_check_endpoint(app: Sanic):
    request, response = app.test_client.get("/health_check")

    assert request.method.lower() == "get"
    assert response.json == {"health": "ok"}
    assert response.status == 200