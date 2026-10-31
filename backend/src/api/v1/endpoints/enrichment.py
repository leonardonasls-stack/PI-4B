from fastapi import APIRouter, Depends, BackgroundTasks
from src.core.security import get_current_admin
from src.core.services.enrichment_service import run_enrichment_worker

router = APIRouter()

@router.post("/sync-osm", summary="Disparar Enriquecimento via OpenStreetMap (Overpass API)", dependencies=[Depends(get_current_admin)])
async def sync_osm_data(background_tasks: BackgroundTasks):
    background_tasks.add_task(run_enrichment_worker)
    return {
        "status": "iniciado",
        "message": "Bot do OpenStreetMap disparado em segundo plano com sucesso! Os novos postos de Maceió serão inseridos de forma idempotente."
    }
