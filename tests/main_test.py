import pytest
import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_ingredient_route(client):
    response = client.get('/ingredient')
    assert response.status_code == 200