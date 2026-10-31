import os
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.config import settings
from src.database.connection import get_db
from src.core.services.city_service import CityService
from src.core.services.point_service import PointService

views_router = APIRouter(include_in_schema=False)

def get_templates_dir() -> str:
    possible_paths = [
        settings.TEMPLATES_DIR,
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "frontend", "templates")),
        os.path.abspath("frontend/templates")
    ]
    for p in possible_paths:
        if os.path.isdir(p):
            return p
    return "frontend/templates"

templates = Jinja2Templates(directory=get_templates_dir())

@views_router.get("/", response_class=HTMLResponse)
async def home_view(request: Request, db: AsyncSession = Depends(get_db)):
    city_service = CityService(db)
    point_service = PointService(db)
    
    cities = await city_service.list_cities()
    initial_city_id = cities[0].id if cities else 1
    points = []
    if cities:
        points = await point_service.list_by_city(initial_city_id)
        
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "cities": cities,
            "selected_city_id": initial_city_id,
            "points": points
        }
    )

@views_router.get("/admin", response_class=HTMLResponse)
async def admin_view(request: Request, db: AsyncSession = Depends(get_db)):
    city_service = CityService(db)
    cities = await city_service.list_cities()
    return templates.TemplateResponse(
        "admin.html",
        {
            "request": request,
            "cities": cities
        }
    )
