import requests
from typing import List, Dict, Any
from sqlalchemy import text
from src.database.connection import AsyncSessionLocal

OVERPASS_URL = "http://overpass-api.de/api/interpreter"

def fetch_osm_health_centers_maceio() -> List[Dict[str, Any]]:
    overpass_query = """
    [out:json];
    area["name"="Maceió"]["admin_level"="8"]->.searchArea;
    (
      node["amenity"="clinic"](area.searchArea);
      way["amenity"="clinic"](area.searchArea);
      node["healthcare"="centre"](area.searchArea);
      way["healthcare"="centre"](area.searchArea);
    );
    out center;
    """

    try:
        response = requests.post(OVERPASS_URL, data={'data': overpass_query}, timeout=30)
        if response.status_code != 200:
            return []

        data = response.json()
        points = []

        for el in data.get('elements', []):
            tags = el.get('tags', {})
            name = tags.get('name')
            if not name:
                continue

            lat = el.get('lat') or el.get('center', {}).get('lat')
            lon = el.get('lon') or el.get('center', {}).get('lon')

            street = tags.get('addr:street', 'Endereço não informado no OSM')
            neighborhood = tags.get('addr:suburb', 'Maceió')

            points.append({
                "city_id": 1,
                "name": name.strip(),
                "neighborhood": neighborhood.strip(),
                "address": street.strip(),
                "latitude": float(lat) if lat else None,
                "longitude": float(lon) if lon else None
            })

        return points
    except Exception as e:
        print(f"[OSM BOT] Falha na requisição Overpass: {e}")
        return []

async def run_enrichment_worker() -> int:
    extracted_points = fetch_osm_health_centers_maceio()
    if not extracted_points:
        return 0

    inserted_count = 0
    async with AsyncSessionLocal() as session:
        for p in extracted_points:
            stmt = text("""
                INSERT INTO vaccination_points (city_id, name, neighborhood, address, latitude, longitude)
                VALUES (:city_id, :name, :neighborhood, :address, :latitude, :longitude)
                ON CONFLICT (city_id, name) DO NOTHING
                RETURNING id;
            """)

            res = await session.execute(stmt, p)
            new_id = res.scalar()
            
            if new_id:
                inserted_count += 1
                for vac_id in [1, 2, 3, 4]:
                    await session.execute(
                        text("INSERT INTO point_vaccines (point_id, vaccine_id) VALUES (:p, :v) ON CONFLICT DO NOTHING;"),
                        {"p": new_id, "v": vac_id}
                    )
        
        await session.commit()

    return inserted_count

if __name__ == "__main__":
    import asyncio
    total = asyncio.run(run_enrichment_worker())
    print(f"[OSM BOT] Concluído! {total} postos foram inseridos no banco.")
