from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from fastapi import HTTPException, status
from src.database.models.entities import City
from src.schemas.city import CityListResponse, CityDetailResponse

class CityService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_cities(self) -> List[CityListResponse]:
        result = await self.db.execute(select(City).order_by(City.id))
        cities = list(result.scalars().all())
        return [CityListResponse(id=c.id, name=c.name) for c in cities]

    async def get_city_by_id(self, city_id: int) -> CityDetailResponse:
        result = await self.db.execute(
            select(City)
            .options(selectinload(City.state))
            .where(City.id == city_id)
        )
        city = result.scalars().first()
        if not city:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cidade não encontrada"
            )
        state_name = city.state.name if city.state else "Alagoas"
        return CityDetailResponse(id=city.id, name=city.name, state=state_name)
