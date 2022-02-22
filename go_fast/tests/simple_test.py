import pytest
from go_fast import zoom

@pytest.fixture
def app():
    return zoom()

def test_basic_test_client(app):
    request, response = app.test_client.get("/")

    assert request.method.lower() == "get"
    assert response.body == b"foo"
    assert response.status == 200