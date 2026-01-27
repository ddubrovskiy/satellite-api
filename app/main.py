from fastapi import FastAPI, HTTPException
from typing import List
import uuid
from .models import Satellite, SatelliteCreate

app = FastAPI(title="Satellite API")

satellites_db = {}

@app.get("/satellites", response_model=List[Satellite])
def get_satellites():
    return list(satellites_db.values())

@app.post("/satellites", response_model=Satellite)
def create_satellite(satellite: SatelliteCreate):
    sat_id = str(uuid.uuid4())
    new_sat = Satellite(id=sat_id, **satellite.dict())
    satellites_db[sat_id] = new_sat
    return new_sat