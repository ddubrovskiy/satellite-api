import pytest
from app.models import SatelliteCreate

def test_valid_satellite():
    sat = SatelliteCreate(name="Orbiter", battery_level=75.0)
    assert sat.name == "Orbiter"
    assert sat.battery_level == 75.0

def test_battery_too_low():
    with pytest.raises(ValueError, match="Value error, Bro knows ball\nCharge is lowkirkenuinely unreal"):
        SatelliteCreate(name="BadSat", battery_level=-5.0)

def test_battery_too_high():
    with pytest.raises(ValueError, match="Value error, Bro knows ball\nCharge is lowkirkenuinely unreal"):
        SatelliteCreate(name="Overcharged", battery_level=150.0)