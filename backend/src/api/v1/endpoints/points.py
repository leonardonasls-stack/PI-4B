from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.connection import get_db
from src.core.security import get_current_admin
from src.core.services.point_service import PointService
from src.schemas.point import (
    VaccinationPointResponse,
    VaccinationPointCreate,
    VaccinationPointUpdate
)

router = APIRouter()

@router.get("/detail/{point_id}", response_model=VaccinationPointResponse, summary="Obter Detalhes de um Posto por ID")
async def get_point_by_id(point_id: int, db: AsyncSession = Depends(get_db)):
    service = PointService(db)
    return await service.get_by_id(point_id)

@router.get("/{city_id}", response_model=List[VaccinationPointResponse], summary="Listar Pontos de Vacinação por Cidade (RF-03)")
async def get_points_by_city(city_id: int, db: AsyncSession = Depends(get_db)):
    service = PointService(db)
    return await service.list_by_city(city_id)

@router.post("", status_code=status.HTTP_201_CREATED, summary="Inserção Administrativa de Postos (RF-05)", dependencies=[Depends(get_current_admin)])
async def create_vaccination_point(
    payload: VaccinationPointCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PointService(db)
    new_id = await service.create_point(payload)
    return {"message": "Ponto de vacinação cadastrado com sucesso", "id": new_id}

@router.put("/{point_id}", response_model=VaccinationPointResponse, summary="Atualização Cadastral de Posto (CRUD)", dependencies=[Depends(get_current_admin)])
async def update_vaccination_point(
    point_id: int,
    payload: VaccinationPointUpdate,
    db: AsyncSession = Depends(get_db)
):
    service = PointService(db)
    return await service.update_point(point_id, payload)

@router.delete("/{point_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Exclusão de Posto (CRUD)", dependencies=[Depends(get_current_admin)])
async def delete_vaccination_point(
    point_id: int,
    db: AsyncSession = Depends(get_db)
):
    service = PointService(db)
    await service.delete_point(point_id)
    return None
