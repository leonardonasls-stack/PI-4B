from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.connection import get_db
from src.core.services.city_service import CityService
from src.schemas.city import CityListResponse, CityDetailResponse

router = APIRouter()

@router.get("", response_model=List[CityListResponse], summary="Listar Cidades de Alagoas (RF-01)")
async def get_cities(db: AsyncSession = Depends(get_db)):
    service = CityService(db)
    return await service.list_cities()

@router.get("/{id}", response_model=CityDetailResponse, summary="Detalhes da Cidade por ID (RF-02)")
async def get_city_by_id(id: int, db: AsyncSession = Depends(get_db)):
    service = CityService(db)
    return await service.get_city_by_id(id)
