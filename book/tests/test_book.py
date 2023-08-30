from httpx import AsyncClient


async def test_create_book(async_client: AsyncClient):
    response = await async_client.post('/book/', json={
        'title': 'Book1',
        'author_id': 2,
    })
    assert response.status_code == 200


async def test_get_books(async_client: AsyncClient):
    response = await async_client.get('/book/')
    assert response.status_code == 200


async def test_get_book(async_client: AsyncClient):
    response = await async_client.get('/book/1')
    assert response.status_code == 200


async def test_update_book(async_client: AsyncClient):
    response = await async_client.put('/book/1', json={
        'title': 'Book2',
    })
    assert response.status_code == 200