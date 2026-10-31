import requests
from typing import List, Dict, Any, Optional
from sqlalchemy import text
from src.database.connection import AsyncSessionLocal

NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
OVERPASS_URLS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
    "https://lz4.overpass-api.de/api/interpreter"
]

def fetch_osm_health_centers_maceio() -> List[Dict[str, Any]]:
    """
    Busca unidades de saúde e postos em Maceió via OpenStreetMap.
    Utiliza consultas via Nominatim (com fallback em Overpass API) garantindo resiliência e dados reais.
    """
    headers = {"User-Agent": "VacinaAlagoasApp/1.0 (academic.project.alagoas@gmail.com)"}
    points: List[Dict[str, Any]] = []
    seen_names = set()

    # 1. Estratégia Principal: Busca assertiva via Nominatim OpenStreetMap
    queries = [
        "UBS Maceió",
        "USF Maceió",
        "Unidade de Saúde Maceió",
        "Posto de Saúde Maceió",
        "Centro de Saúde Maceió"
    ]

    for q in queries:
        try:
            params = {"q": q, "format": "json", "limit": 10, "addressdetails": 1}
            r = requests.get(NOMINATIM_URL, params=params, headers=headers, timeout=6)
            if r.status_code == 200:
                for item in r.json():
                    display_parts = item.get("display_name", "").split(",")
                    name = display_parts[0].strip() if display_parts else ""
                    if not name or name in seen_names:
                        continue

                    seen_names.add(name)
                    addr = item.get("address", {})
                    neighborhood = (
                        addr.get("suburb") or 
                        addr.get("neighbourhood") or 
                        addr.get("city_district") or 
                        "Maceió"
                    ).strip()
                    street = (
                        addr.get("road") or 
                        addr.get("street") or 
                        (display_parts[1].strip() if len(display_parts) > 1 else "Endereço via OpenStreetMap")
                    ).strip()

                    lat = item.get("lat")
                    lon = item.get("lon")

                    points.append({
                        "city_id": 1,
                        "name": name,
                        "neighborhood": neighborhood,
                        "address": street,
                        "latitude": float(lat) if lat else None,
                        "longitude": float(lon) if lon else None,
                        "source": "OpenStreetMap"
                    })
        except Exception as e:
            print(f"[OSM BOT] Erro na consulta Nominatim '{q}': {e}")

    # 2. Se Nominatim não trouxe resultados, tenta Overpass API
    if not points:
        overpass_query = """
        [out:json][timeout:20];
        (
          node["amenity"="clinic"](-9.75,-35.85,-9.55,-35.65);
          node["healthcare"="centre"](-9.75,-35.85,-9.55,-35.65);
        );
        out center 25;
        """
        for server in OVERPASS_URLS:
            try:
                resp = requests.post(server, data={"data": overpass_query}, headers=headers, timeout=12)
                if resp.status_code == 200:
                    data = resp.json()
                    for el in data.get("elements", []):
                        tags = el.get("tags", {})
                        name = tags.get("name")
                        if not name or name in seen_names:
                            continue
                        seen_names.add(name)
                        lat = el.get("lat") or el.get("center", {}).get("lat")
                        lon = el.get("lon") or el.get("center", {}).get("lon")
                        points.append({
                            "city_id": 1,
                            "name": name.strip(),
                            "neighborhood": tags.get("addr:suburb", "Maceió").strip(),
                            "address": tags.get("addr:street", "Endereço via OpenStreetMap").strip(),
                            "latitude": float(lat) if lat else None,
                            "longitude": float(lon) if lon else None,
                            "source": "Overpass API"
                        })
                    if points:
                        break
            except Exception as e:
                print(f"[OSM BOT] Falha no servidor Overpass {server}: {e}")

    return points

async def save_points_to_database(points_to_save: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Insere no banco de dados apenas os postos confirmados pelo administrador.
    """
    inserted_count = 0
    ignored_count = 0
    saved_ids = []

    async with AsyncSessionLocal() as session:
        for p in points_to_save:
            stmt = text("""
                INSERT INTO vaccination_points (city_id, name, neighborhood, address, latitude, longitude)
                VALUES (:city_id, :name, :neighborhood, :address, :latitude, :longitude)
                ON CONFLICT (city_id, name) DO NOTHING
                RETURNING id;
            """)

            res = await session.execute(stmt, {
                "city_id": p.get("city_id", 1),
                "name": p["name"],
                "neighborhood": p.get("neighborhood", "Maceió"),
                "address": p.get("address", "Endereço via OpenStreetMap"),
                "latitude": p.get("latitude"),
                "longitude": p.get("longitude")
            })
            new_id = res.scalar()

            if new_id:
                inserted_count += 1
                saved_ids.append(new_id)
                # Vincula vacinas padrão do calendário básico
                for vac_id in [1, 2, 3, 4]:
                    await session.execute(
                        text("INSERT INTO point_vaccines (point_id, vaccine_id) VALUES (:p, :v) ON CONFLICT DO NOTHING;"),
                        {"p": new_id, "v": vac_id}
                    )
            else:
                ignored_count += 1

        await session.commit()

    return {
        "inserted": inserted_count,
        "ignored": ignored_count,
        "saved_ids": saved_ids
    }

async def run_enrichment_worker() -> int:
    """Worker legado para execução automática sem confirmação prévia."""
    extracted = fetch_osm_health_centers_maceio()
    if not extracted:
        return 0
    res = await save_points_to_database(extracted)
    return res["inserted"]
