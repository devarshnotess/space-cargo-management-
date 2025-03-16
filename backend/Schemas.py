from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema for Item
class ItemBase(BaseModel):
    item_id: str
    name: str
    width: float
    depth: float
    height: float
    mass: float
    priority: int
    expiry_date: datetime
    usage_limit: int
    preferred_zone: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    container_id: Optional[int] = None
    pos_width: float = 0
    pos_depth: float = 0
    pos_height: float = 0
    status: str = "active"

    class Config:
        orm_mode = True

# Schema for Container
class ContainerBase(BaseModel):
    container_id: str
    zone: str
    width: float
    depth: float
    height: float

class ContainerCreate(ContainerBase):
    pass

class Container(ContainerBase):
    id: int

    class Config:
        orm_mode = True

# Schema for Simulation
class SimulationBase(BaseModel):
    current_date: datetime

class SimulationCreate(SimulationBase):
    pass

class Simulation(SimulationBase):
    id: int

    class Config:
        orm_mode = True
      
