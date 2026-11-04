import pytest
import pytest_asyncio
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import NullPool
from src.app.config import settings
from src.app.main import app
from src.database.connection import get_db

@pytest_asyncio.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    test_engine = create_async_engine(settings.DATABASE_URL, poolclass=NullPool)
    TestSessionLocal = async_sessionmaker(bind=test_engine, class_=AsyncSession, expire_on_commit=False)

    async def override_get_db() -> AsyncGenerator[AsyncSession, None]:
        async with TestSessionLocal() as session:
            yield session

    app.dependency_overrides[get_db] = override_get_db

    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac

    app.dependency_overrides.clear()
    await test_engine.dispose()

@pytest.mark.asyncio
async def test_get_cities_returns_200(client: AsyncClient):
    response = await client.get("/cities")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 2
    names = [c["name"] for c in data]
    assert "Maceió" in names
    assert "Arapiraca" in names

@pytest.mark.asyncio
async def test_get_city_by_id_success(client: AsyncClient):
    response = await client.get("/cities/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Maceió"
    assert data["state"] == "Alagoas"

@pytest.mark.asyncio
async def test_get_city_by_id_not_found(client: AsyncClient):
    response = await client.get("/cities/9999")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_get_city_by_id_invalid(client: AsyncClient):
    response = await client.get("/cities/invalido")
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_get_vaccination_points_by_city(client: AsyncClient):
    response = await client.get("/vaccination-points/1")
    assert response.status_code == 200
    points = response.json()
    assert isinstance(points, list)
    assert len(points) >= 1
    assert "name" in points[0]
    assert "vaccines" in points[0]
    assert isinstance(points[0]["vaccines"], list)

@pytest.mark.asyncio
async def test_auth_login_invalid_credentials(client: AsyncClient):
    response = await client.post("/auth/login", data={"username": "wrong", "password": "wrong"})
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_create_point_unauthorized(client: AsyncClient):
    payload = {"city_id": 1, "name": "Posto Teste"}
    response = await client.post("/vaccination-points", json=payload)
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_update_point_unauthorized(client: AsyncClient):
    payload = {"name": "Posto Alterado"}
    response = await client.put("/vaccination-points/1", json=payload)
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_delete_point_unauthorized(client: AsyncClient):
    response = await client.delete("/vaccination-points/1")
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_get_point_detail_not_found(client: AsyncClient):
    response = await client.get("/vaccination-points/detail/999999")
    assert response.status_code == 404
