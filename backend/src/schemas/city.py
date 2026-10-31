from pydantic import BaseModel, ConfigDict

class CityBase(BaseModel):
    name: str

class CityCreate(CityBase):
    state_id: int

class CityListResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class CityDetailResponse(BaseModel):
    id: int
    name: str
    state: str

    model_config = ConfigDict(from_attributes=True)
