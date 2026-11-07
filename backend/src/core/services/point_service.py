from typing import List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from sqlalchemy.future import select
from fastapi import HTTPException, status
from src.database.models.entities import City, VaccinationPoint, point_vaccines
from src.schemas.point import VaccinationPointResponse, VaccinationPointCreate, VaccinationPointUpdate

class PointService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def list_by_city(self, city_id: int, q: Optional[str] = None) -> List[VaccinationPointResponse]:
        # Validação de existência da cidade (RF-03)
        city_res = await self.db.execute(select(City).where(City.id == city_id))
        city = city_res.scalars().first()
        if not city:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cidade especificada não existe"
            )

        # Consulta otimizada com agregação nativa de vacinas no PostgreSQL e filtro textual/CEP
        sql = """
            SELECT 
                vp.id,
                vp.name,
                vp.neighborhood,
                vp.address,
                vp.latitude,
                vp.longitude,
                COALESCE(
                    ARRAY_REMOVE(ARRAY_AGG(v.name ORDER BY v.name), NULL), 
                    '{}'
                ) AS vaccines
            FROM vaccination_points vp
            LEFT JOIN point_vaccines pv ON vp.id = pv.point_id
            LEFT JOIN vaccines v ON pv.vaccine_id = v.id
            WHERE vp.city_id = :city_id
        """
        params = {"city_id": city_id}
        if q and q.strip():
            sql += """
                AND (
                    vp.name ILIKE :q
                    OR vp.neighborhood ILIKE :q
                    OR vp.address ILIKE :q
                )
            """
            params["q"] = f"%{q.strip()}%"

        sql += """
            GROUP BY vp.id, vp.name, vp.neighborhood, vp.address, vp.latitude, vp.longitude
            ORDER BY vp.name ASC;
        """

        result = await self.db.execute(text(sql), params)
        rows = result.mappings().all()

        return [
            VaccinationPointResponse(
                id=r["id"],
                name=r["name"],
                neighborhood=r["neighborhood"],
                address=r["address"],
                latitude=float(r["latitude"]) if r["latitude"] is not None else None,
                longitude=float(r["longitude"]) if r["longitude"] is not None else None,
                vaccines=r["vaccines"]
            )
            for r in rows
        ]

    async def get_by_id(self, point_id: int) -> VaccinationPointResponse:
        query = text("""
            SELECT 
                vp.id,
                vp.name,
                vp.neighborhood,
                vp.address,
                vp.latitude,
                vp.longitude,
                COALESCE(
                    ARRAY_REMOVE(ARRAY_AGG(v.name ORDER BY v.name), NULL), 
                    '{}'
                ) AS vaccines
            FROM vaccination_points vp
            LEFT JOIN point_vaccines pv ON vp.id = pv.point_id
            LEFT JOIN vaccines v ON pv.vaccine_id = v.id
            WHERE vp.id = :point_id
            GROUP BY vp.id, vp.name, vp.neighborhood, vp.address, vp.latitude, vp.longitude;
        """)
        result = await self.db.execute(query, {"point_id": point_id})
        r = result.mappings().first()
        if not r:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ponto de vacinação não encontrado"
            )

        return VaccinationPointResponse(
            id=r["id"],
            name=r["name"],
            neighborhood=r["neighborhood"],
            address=r["address"],
            latitude=float(r["latitude"]) if r["latitude"] is not None else None,
            longitude=float(r["longitude"]) if r["longitude"] is not None else None,
            vaccines=r["vaccines"]
        )

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

    async def update_point(self, point_id: int, payload: VaccinationPointUpdate) -> VaccinationPointResponse:
        point_res = await self.db.execute(select(VaccinationPoint).where(VaccinationPoint.id == point_id))
        point = point_res.scalars().first()
        if not point:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ponto de vacinação não encontrado"
            )

        if payload.city_id is not None:
            city_res = await self.db.execute(select(City).where(City.id == payload.city_id))
            if not city_res.scalars().first():
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Cidade informada não existe"
                )
            point.city_id = payload.city_id

        if payload.name is not None:
            point.name = payload.name
        if payload.neighborhood is not None:
            point.neighborhood = payload.neighborhood
        if payload.address is not None:
            point.address = payload.address
        if payload.latitude is not None:
            point.latitude = payload.latitude
        if payload.longitude is not None:
            point.longitude = payload.longitude

        if payload.vaccine_ids is not None:
            await self.db.execute(
                point_vaccines.delete().where(point_vaccines.c.point_id == point_id)
            )
            for vac_id in payload.vaccine_ids:
                await self.db.execute(
                    point_vaccines.insert().values(point_id=point.id, vaccine_id=vac_id)
                )

        await self.db.commit()
        return await self.get_by_id(point_id)

    async def delete_point(self, point_id: int) -> None:
        point_res = await self.db.execute(select(VaccinationPoint).where(VaccinationPoint.id == point_id))
        point = point_res.scalars().first()
        if not point:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ponto de vacinação não encontrado"
            )

        await self.db.delete(point)
        await self.db.commit()
