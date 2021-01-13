from typing import Dict
from ..ids.unit_typeid import UnitTypeId


TURN_RATE: Dict[UnitTypeId, float] = {
    UnitTypeId.STALKER: 999.8437,
    UnitTypeId.ZEALOT: 999.8437,
}


DAMAGE_POINT: Dict[UnitTypeId, float] = {
    UnitTypeId.STALKER: 0.1193,
    UnitTypeId.ZEALOT: 0.,
    UnitTypeId.PROBE: 0.1193,
    UnitTypeId.ADEPT: 0.1193,
    UnitTypeId.MARINE: 0.0357,
}
