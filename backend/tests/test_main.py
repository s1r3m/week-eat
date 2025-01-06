import httpx
import pytest_asyncio

from settings import APP_HOST


@pytest_asyncio.fixture
async def client():
    async with httpx.AsyncClient() as client:
        yield client


async def test_ping__always__pong_response(client):
    response = await client.get(f'{APP_HOST}/ping')

    assert response.status_code == 200
    assert response.json() == {"state": "pong"}
