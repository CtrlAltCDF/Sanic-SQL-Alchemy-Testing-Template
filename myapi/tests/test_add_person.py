import pytest
from sanic import Sanic
from myapi import app as myapi_app

@pytest.fixture(scope="function")
def app() -> Sanic:
    print("called this")
    return myapi_app("test")

def test_add_person_to_db(app: Sanic):
    request, response = app.test_client.post("/people")

    assert request.method.lower() == "post"
    assert response.json == {"id": 1, "name" : "Test User"}
    assert response.status == 200