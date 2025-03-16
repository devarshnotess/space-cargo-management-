from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Container)
def create_container(container: schemas.ContainerCreate, db: Session = Depends(get_db)):
    if crud.get_container_by_container_id(db, container.container_id):
        raise HTTPException(status_code=400, detail="Container already registered")
    return crud.create_container(db, container)

@router.get("/{container_id}", response_model=schemas.Container)
def read_container(container_id: int, db: Session = Depends(get_db)):
    db_container = crud.get_container(db, container_id)
    if db_container is None:
        raise HTTPException(status_code=404, detail="Container not found")
    return db_container

@router.get("/", response_model=list[schemas.Container])
def read_containers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    containers = crud.get_containers(db, skip=skip, limit=limit)
    return containers

@router.put("/{container_id}", response_model=schemas.Container)
def update_container(container_id: int, container: schemas.ContainerCreate, db: Session = Depends(get_db)):
    db_container = crud.update_container(db, container_id, container)
    if db_container is None:
        raise HTTPException(status_code=404, detail="Container not found")
    return db_container

@router.delete("/{container_id}", response_model=schemas.Container)
def delete_container(container_id: int, db: Session = Depends(get_db)):
    db_container = crud.delete_container(db, container_id)
    if db_container is None:
        raise HTTPException(status_code=404, detail="Container not found")
    return db_container
