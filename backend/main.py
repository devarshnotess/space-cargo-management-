from fastapi import FastAPI
from routes import items, containers, simulation
from database import engine, Base

# Create all database tables (if they do not exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Space Cargo Management API with Advanced Features")

# Include routers for items, containers, and simulation
app.include_router(items.router, prefix="/api/items", tags=["Items"])
app.include_router(containers.router, prefix="/api/containers", tags=["Containers"])
app.include_router(simulation.router, prefix="/api/simulation", tags=["Simulation"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Advanced Space Cargo Management API"}
