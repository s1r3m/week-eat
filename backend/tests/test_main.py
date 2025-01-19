from fastapi.testclient import TestClient
import pytest

from week_eat_planner.config import settings
from week_eat_planner.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_settings__always__settings_present():
    assert settings


def test_app_instance__bad_path__not_found_response(client):
    response = client.get("/test")

    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
