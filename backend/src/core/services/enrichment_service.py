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

def fetch_osm_health_centers(escopo: str = "alagoas") -> List[Dict[str, Any]]:
    """
    Busca unidades de saúde e postos via OpenStreetMap por escopo:
    - 'alagoas': Varredura estadual (Maceió, Arapiraca e cidades pólo de AL)
    - 'maceio': Apenas capital Maceió
    - 'arapiraca': Apenas região agreste / Arapiraca
    """
    headers = {"User-Agent": "VacinaAlagoasApp/1.0 (academic.project.alagoas@gmail.com)"}
    points: List[Dict[str, Any]] = []
    seen_names = set()

    escopo_lower = escopo.lower()
    
    if escopo_lower == "maceio":
        queries = [
            ("UBS Maceió", 1, "Maceió"),
            ("USF Maceió", 1, "Maceió"),
            ("Posto de Saúde Maceió", 1, "Maceió"),
            ("Centro de Saúde Maceió", 1, "Maceió")
        ]
    elif escopo_lower == "arapiraca":
        queries = [
            ("UBS Arapiraca", 2, "Arapiraca"),
            ("USF Arapiraca", 2, "Arapiraca"),
            ("Posto de Saúde Arapiraca", 2, "Arapiraca"),
            ("Centro de Saúde Arapiraca", 2, "Arapiraca")
        ]
    else:  # Todo o estado de Alagoas
        queries = [
            ("UBS Maceió Alagoas", 1, "Maceió"),
            ("USF Maceió Alagoas", 1, "Maceió"),
            ("UBS Arapiraca Alagoas", 2, "Arapiraca"),
            ("USF Arapiraca Alagoas", 2, "Arapiraca"),
            ("Posto de Saúde Alagoas", 1, "Maceió"),
            ("Unidade de Saúde Alagoas", 1, "Maceió")
        ]

    for q, default_city_id, default_city_name in queries:
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
                    
                    # Detectar cidade
                    city_detected = addr.get("city") or addr.get("town") or addr.get("municipality") or default_city_name
                    city_id = 2 if "arapiraca" in city_detected.lower() else 1

                    neighborhood = (
                        addr.get("suburb") or 
                        addr.get("neighbourhood") or 
                        addr.get("city_district") or 
                        city_detected
                    ).strip()
                    
                    street = (
                        addr.get("road") or 
                        addr.get("street") or 
                        (display_parts[1].strip() if len(display_parts) > 1 else "Endereço via OpenStreetMap")
                    ).strip()

                    lat = item.get("lat")
                    lon = item.get("lon")

                    points.append({
                        "city_id": city_id,
                        "name": name,
                        "neighborhood": neighborhood,
                        "address": street,
                        "latitude": float(lat) if lat else None,
                        "longitude": float(lon) if lon else None,
                        "source": "OpenStreetMap Nominatim"
                    })
        except Exception as e:
            print(f"[OSM BOT] Erro na consulta Nominatim '{q}': {e}")

    # Fallback Overpass se nada vier pelo Nominatim
    if not points:
        if escopo_lower == "arapiraca":
            bbox = "(-9.85,-36.75,-9.65,-36.55)"
            c_id = 2
        else:
            bbox = "(-9.75,-35.85,-9.55,-35.65)"
            c_id = 1

        overpass_query = f"""
        [out:json][timeout:20];
        (
          node["amenity"="clinic"]{bbox};
          node["healthcare"="centre"]{bbox};
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
                            "city_id": c_id,
                            "name": name.strip(),
                            "neighborhood": tags.get("addr:suburb", "Centro").strip(),
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

def fetch_osm_health_centers_maceio() -> List[Dict[str, Any]]:
    return fetch_osm_health_centers(escopo="maceio")

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
    extracted = fetch_osm_health_centers(escopo="alagoas")
    if not extracted:
        return 0
    res = await save_points_to_database(extracted)
    return res["inserted"]
