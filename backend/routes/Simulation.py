from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import logic
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/simulate")
def simulate_days(num_days: int, db: Session = Depends(get_db)):
    sim = logic.simulate_days(db, num_days)
    return {"new_simulation_date": sim.current_date}
