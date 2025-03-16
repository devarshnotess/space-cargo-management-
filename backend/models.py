import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Container(Base):
    __tablename__ = "containers"
    id = Column(Integer, primary_key=True, index=True)
    container_id = Column(String, unique=True, index=True)
    zone = Column(String, index=True)
    width = Column(Float)
    depth = Column(Float)
    height = Column(Float)
    # Relationship to items stored in this container
    items = relationship("Item", back_populates="container")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    item_id = Column(String, unique=True, index=True)
    name = Column(String, index=True)
    width = Column(Float)
    depth = Column(Float)
    height = Column(Float)
    mass = Column(Float)
    priority = Column(Integer)
    expiry_date = Column(DateTime, default=datetime.datetime.utcnow)
    usage_limit = Column(Integer)
    preferred_zone = Column(String)
    container_id = Column(Integer, ForeignKey("containers.id"), nullable=True)
    container = relationship("Container", back_populates="items")
    # Placement coordinates within the container
    pos_width = Column(Float, default=0)
    pos_depth = Column(Float, default=0)
    pos_height = Column(Float, default=0)
    # Status of the item ("active" or "waste")
    status = Column(String, default="active")

# Model to track the current simulation date
class Simulation(Base):
    __tablename__ = "simulation"
    id = Column(Integer, primary_key=True)
    current_date = Column(DateTime, default=datetime.datetime.utcnow)
