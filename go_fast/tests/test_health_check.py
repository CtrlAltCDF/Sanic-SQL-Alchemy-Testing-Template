import pytest
from go_fast import zoom

@pytest.fixture
def app():
    return zoom(testing=True)

def test_basic_test_client(app):
    request, response = app.test_client.get("/health_check")

    assert request.method.lower() == "get"
    assert response.json == {"health": "ok"}
    assert response.status == 200