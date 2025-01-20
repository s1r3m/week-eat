import pytest
from fastapi.testclient import TestClient

from week_eat_planner.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)
