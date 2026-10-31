from typing import List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from sqlalchemy.future import select
from fastapi import HTTPException, status
from src.database.models.entities import City, VaccinationPoint, point_vaccines
from src.schemas.point import VaccinationPointResponse, VaccinationPointCreate

class PointService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_by_city(self, city_id: int) -> List[VaccinationPointResponse]:
        # Validação de existência da cidade (RF-03)
        city_res = await self.db.execute(select(City).where(City.id == city_id))
        city = city_res.scalars().first()
        if not city:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cidade especificada não existe"
            )

        # Consulta otimizada com agregação nativa de vacinas no PostgreSQL
        query = text("""
            SELECT 
                vp.id,
                vp.name,
                vp.neighborhood,
                vp.address,
                COALESCE(
                    ARRAY_REMOVE(ARRAY_AGG(v.name ORDER BY v.name), NULL), 
                    '{}'
                ) AS vaccines
            FROM vaccination_points vp
            LEFT JOIN point_vaccines pv ON vp.id = pv.point_id
            LEFT JOIN vaccines v ON pv.vaccine_id = v.id
            WHERE vp.city_id = :city_id
            GROUP BY vp.id, vp.name, vp.neighborhood, vp.address
            ORDER BY vp.name ASC;
        """)

        result = await self.db.execute(query, {"city_id": city_id})
        rows = result.mappings().all()

        return [
            VaccinationPointResponse(
                id=r["id"],
                name=r["name"],
                neighborhood=r["neighborhood"],
                address=r["address"],
                vaccines=r["vaccines"]
            )
            for r in rows
        ]

    async def create_point(self, payload: VaccinationPointCreate) -> int:
        city_res = await self.db.execute(select(City).where(City.id == payload.city_id))
        city = city_res.scalars().first()
        if not city:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cidade informada não existe"
            )

        new_point = VaccinationPoint(
            city_id=payload.city_id,
            name=payload.name,
            neighborhood=payload.neighborhood,
            address=payload.address,
            latitude=payload.latitude,
            longitude=payload.longitude
        )
        self.db.add(new_point)
        await self.db.flush()

        for vac_id in payload.vaccine_ids:
            await self.db.execute(
                point_vaccines.insert().values(point_id=new_point.id, vaccine_id=vac_id)
            )

        await self.db.commit()
        return new_point.id
