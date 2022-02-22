import pytest
from sanic import Sanic, response, text

from app import generate_app

@pytest.fixture
def app():
    return generate_app()

def test_basic_test_client(app):
    request, response = app.test_client.get("/")

    assert request.method.lower() == "get"
    assert response.body == b"foo"
    assert response.status == 200