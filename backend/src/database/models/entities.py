from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text, Table, func
from sqlalchemy.orm import relationship
from src.database.models.base import Base

point_vaccines = Table(
    "point_vaccines",
    Base.metadata,
    Column("point_id", Integer, ForeignKey("vaccination_points.id", ondelete="CASCADE"), primary_key=True),
    Column("vaccine_id", Integer, ForeignKey("vaccines.id", ondelete="CASCADE"), primary_key=True)
)

class AdminUser(Base):
    __tablename__ = "admin_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    uf = Column(String(2), unique=True, nullable=False)

    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    state_id = Column(Integer, ForeignKey("states.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(120), nullable=False)

    state = relationship("State", back_populates="cities")
    vaccination_points = relationship("VaccinationPoint", back_populates="city", cascade="all, delete-orphan")

class Vaccine(Base):
    __tablename__ = "vaccines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    points = relationship("VaccinationPoint", secondary=point_vaccines, back_populates="vaccines")

class VaccinationPoint(Base):
    __tablename__ = "vaccination_points"

    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey("cities.id", ondelete="CASCADE"), nullable=False, index=True)
    name = Column(String(150), nullable=False)
    neighborhood = Column(String(100), nullable=True)
    logradouro = Column(String(150), nullable=True)
    number = Column(String(20), nullable=True)
    cep = Column(String(10), nullable=True)
    address = Column(String(200), nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    city = relationship("City", back_populates="vaccination_points")
    vaccines = relationship("Vaccine", secondary=point_vaccines, back_populates="points")
