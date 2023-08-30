from httpx import AsyncClient

from tests.conftest import async_client


async def test_authors(async_client: AsyncClient):
    response = await async_client.get('author/')
    assert response.status_code == 200
    

async def test_create_author(async_client: AsyncClient):
    response = await async_client.post('author/', json={
        'first_name': 'Ivan',
        'last_name': 'Ivanov',
    })
    assert response.status_code == 200
    print(response.read())


async def test_update_author(async_client: AsyncClient):
    response = await async_client.put('author/1', json={
        'first_name': 'Igor',
        'last_name': 'Ivanov',
    })
    assert response.status_code == 200
    print(response.read())