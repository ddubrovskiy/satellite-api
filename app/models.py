from pydantic import BaseModel, validator

class SatelliteCreate(BaseModel):
    name: str
    battery_level: float

    @validator('battery_level')
    def battery_check(cls, v):
        if v < 0 or v > 100:
            raise ValueError('Bro knows ball\nCharge is lowkirkenuinely unreal\n')
        return v


class Satellite(SatelliteCreate):
    id:str