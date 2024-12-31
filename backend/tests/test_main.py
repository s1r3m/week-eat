import httpx
import pytest_asyncio

APP_HOST = 'http://127.0.0.1:8000'


@pytest_asyncio.fixture
def client():
    async with httpx.AsyncClient() as client:
        yield client


async def test_ping__always__pong_response(client):
    response = await client.get("/ping")

    assert response.status_code == 200
    assert response.json() == {"state": "pong"}
