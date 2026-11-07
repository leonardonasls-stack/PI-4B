from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Depends, HTTPException, Query, status
from pydantic import BaseModel
from src.core.security import get_current_admin
from src.core.services.enrichment_service import (
    fetch_osm_health_centers,
    fetch_osm_health_centers_maceio,
    save_points_to_database
)

router = APIRouter()

class OsmPointItem(BaseModel):
    city_id: int = 1
    name: str
    neighborhood: str = "Maceió"
    address: str = "Endereço via OpenStreetMap"
    latitude: float | None = None
    longitude: float | None = None
    source: str | None = None

class ConfirmSaveRequest(BaseModel):
    points: List[OsmPointItem]

@router.get("/preview-osm", summary="Listar Resultados da Pesquisa do Bot OSM (Sem Salvar)", dependencies=[Depends(get_current_admin)])
async def preview_osm_data(
    escopo: str = Query("alagoas", description="Escopo territorial da mineração: 'alagoas', 'maceio' ou 'arapiraca'")
):
    """
    Executa a pesquisa e mineração nos dados do OpenStreetMap e retorna
    a lista completa de unidades encontradas para conferência do administrador,
    sem gravar no banco de dados.
    """
    points = fetch_osm_health_centers(escopo=escopo)
    return {
        "status": "sucesso",
        "escopo": escopo,
        "total_encontrados": len(points),
        "results": points
    }

@router.post("/confirm-save", summary="Confirmar e Salvar Postos Minerados no Banco de Dados", dependencies=[Depends(get_current_admin)])
async def confirm_save_osm_data(payload: ConfirmSaveRequest):
    """
    Recebe os postos conferidos/selecionados pelo administrador e
    realiza a gravação efetiva no banco de dados com amarração das vacinas padrão.
    """
    if not payload.points:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nenhum ponto enviado para confirmação e salvamento."
        )

    dict_points = [p.model_dump() for p in payload.points]
    result = await save_points_to_database(dict_points)
    
    return {
        "status": "concluido",
        "message": f"Salvamento concluído! {result['inserted']} novos postos inseridos, {result['ignored']} já existentes ignorados.",
        "inserted_count": result["inserted"],
        "ignored_count": result["ignored"]
    }

@router.post("/sync-osm", summary="Legado: Disparar Enriquecimento Automático", dependencies=[Depends(get_current_admin)])
async def sync_osm_legacy():
    points = fetch_osm_health_centers(escopo="alagoas")
    result = await save_points_to_database(points)
    return {
        "status": "concluido",
        "message": f"Enriquecimento concluído: {result['inserted']} postos adicionados.",
        "detalhes": result
    }
