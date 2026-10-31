from typing import List, Optional
from pydantic import BaseModel, ConfigDict

class VaccinationPointCreate(BaseModel):
    city_id: int
    name: str
    neighborhood: Optional[str] = None
    address: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    vaccine_ids: List[int] = []

class VaccinationPointResponse(BaseModel):
    id: int
    name: str
    neighborhood: Optional[str] = None
    address: Optional[str] = None
    vaccines: List[str] = []

    model_config = ConfigDict(from_attributes=True)
