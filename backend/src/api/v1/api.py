from fastapi import APIRouter
from src.api.v1.endpoints import auth, cities, points, enrichment

api_router = APIRouter()

# Rotas com prefixo v1
api_router.include_router(auth.router, prefix="/auth", tags=["Autenticação Administrativa"])
api_router.include_router(cities.router, prefix="/cities", tags=["Municípios (cities)"])
api_router.include_router(points.router, prefix="/vaccination-points", tags=["Pontos de Vacinação (vaccination-points)"])
api_router.include_router(enrichment.router, prefix="/admin/enrichment", tags=["Bot de Enriquecimento de Dados (OSM)"])
