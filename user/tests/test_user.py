from httpx import AsyncClient


async def test_register(async_client: AsyncClient):
    response = await async_client.post('/auth/register', json={
        'email': 'user@example.com',
        'password': 'test_password',
    })
    assert response.status_code == 201


async def test_login(async_client: AsyncClient):
    response = await async_client.post('/auth/login', json={
        'username': 'user@example.com',
        'password': 'test_password',
    })
    assert response.status_code == 200
    return response.cookies.get('access_token_cookie')


async def test_logout(async_client: AsyncClient):
    token = await test_login(async_client)
    response = await async_client.post('/auth/logout', cookies={'access_token_cookie': token})
    assert response.status_code == 200
    
async def test_refresh(async_client: AsyncClient):
    token = await test_login(async_client)
    response = await async_client.post('/auth/logout', cookies={'access_token_cookie': token})
    assert response.status_code == 200