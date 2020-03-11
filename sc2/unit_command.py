from __future__ import annotations
from typing import Any, Dict, List, Optional, Set, Tuple, Union, TYPE_CHECKING

# from . import unit as unit_module
from .ids.ability_id import AbilityId
from .position import Point2

# Used in unit_command.py and action.py to combine only certain abilities
# TODO fix me
COMBINEABLE_ABILITIES = set()
# COMBINEABLE_ABILITIES: Set[AbilityId] = {
#     AbilityId.MOVE,
#     AbilityId.ATTACK,
#     AbilityId.SCAN_MOVE,
#     AbilityId.SMART,
#     AbilityId.STOP,
#     AbilityId.HOLDPOSITION,
#     AbilityId.PATROL,
#     AbilityId.HARVEST_GATHER,
#     AbilityId.HARVEST_RETURN,
#     AbilityId.EFFECT_REPAIR,
#     AbilityId.RALLY_BUILDING,
#     AbilityId.RALLY_UNITS,
#     AbilityId.RALLY_WORKERS,
#     AbilityId.RALLY_MORPHING_UNIT,
#     AbilityId.LIFT,
#     AbilityId.BURROWDOWN,
#     AbilityId.BURROWUP,
#     AbilityId.SIEGEMODE_SIEGEMODE,
#     AbilityId.UNSIEGE_UNSIEGE,
#     AbilityId.MORPH_LIBERATORAAMODE,
#     AbilityId.EFFECT_STIM,
#     AbilityId.MORPH_UPROOT,
#     AbilityId.EFFECT_BLINK,
#     AbilityId.MORPH_ARCHON,
# }

from typing import Union

if TYPE_CHECKING:
    from .unit import Unit


class UnitCommand:
    def __init__(self, ability: AbilityId, unit: Unit, target: Union[Unit, Point2] = None, queue: bool = False):
        """
        :param ability:
        :param unit:
        :param target:
        :param queue:
        """
        assert ability in AbilityId, f"ability {ability} is not in AbilityId"
        # assert isinstance(unit, unit_module.Unit), f"unit {unit} is of type {type(unit)}"
        # assert target is None or isinstance(
        #     target, (Point2, unit_module.Unit)
        # ), f"target {target} is of type {type(target)}"
        assert isinstance(queue, bool), f"queue flag {queue} is of type {type(queue)}"
        self.ability = ability
        self.unit = unit
        self.target = target
        self.queue = queue

    @property
    def combining_tuple(self):
        return (self.ability, self.target, self.queue, self.ability in COMBINEABLE_ABILITIES)

    def __repr__(self):
        return f"UnitCommand({self.ability}, {self.unit}, {self.target}, {self.queue})"
