from sqlalchemy.orm import Session
import models, schemas
import datetime

# CRUD functions for Items
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_item_by_item_id(db: Session, item_id_str: str):
    return db.query(models.Item).filter(models.Item.item_id == item_id_str).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def update_item(db: Session, item_id: int, updated_item: schemas.ItemCreate):
    db_item = get_item(db, item_id)
    if db_item:
        for key, value in updated_item.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item

# CRUD functions for Containers
def create_container(db: Session, container: schemas.ContainerCreate):
    db_container = models.Container(**container.dict())
    db.add(db_container)
    db.commit()
    db.refresh(db_container)
    return db_container

def get_container(db: Session, container_id: int):
    return db.query(models.Container).filter(models.Container.id == container_id).first()

def get_container_by_container_id(db: Session, container_id_str: str):
    return db.query(models.Container).filter(models.Container.container_id == container_id_str).first()

def get_containers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Container).offset(skip).limit(limit).all()

def update_container(db: Session, container_id: int, updated_container: schemas.ContainerCreate):
    db_container = get_container(db, container_id)
    if db_container:
        for key, value in updated_container.dict().items():
            setattr(db_container, key, value)
        db.commit()
        db.refresh(db_container)
    return db_container

def delete_container(db: Session, container_id: int):
    db_container = get_container(db, container_id)
    if db_container:
        db.delete(db_container)
        db.commit()
    return db_container

# CRUD functions for Simulation
def get_simulation(db: Session):
    return db.query(models.Simulation).first()

def create_simulation(db: Session):
    sim = models.Simulation(current_date=datetime.datetime.utcnow())
    db.add(sim)
    db.commit()
    db.refresh(sim)
    return sim
