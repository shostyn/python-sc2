from __future__ import annotations
import random
import warnings
import math
from itertools import chain
from typing import (
    Any,
    Dict,
    Iterable,
    List,
    Optional,
    Set,
    Tuple,
    Union,
    Generator,
    TYPE_CHECKING,
)

import numpy as np

from .ids.unit_typeid import UnitTypeId
from .position import Point2
from .unit import Unit

warnings.simplefilter("once")

if TYPE_CHECKING:
    from .bot_ai import BotAI


class Units(list):
    """A collection of Unit objects. Makes it easy to select units by selectors."""

    @classmethod
    def from_proto(cls, units, bot_object: BotAI):
        return cls((Unit(u, bot_object=bot_object) for u in units))

    def __init__(self, units, bot_object: BotAI):
        """
        :param units:
        :param bot_object:
        """
        super().__init__(units)
        self._bot_object = bot_object

    def __call__(self, *args, **kwargs):
        return UnitSelection(self, *args, **kwargs)

    def __iter__(self) -> Generator[Unit, None, None]:
        return (item for item in super().__iter__())

    def select(self, *args, **kwargs):
        return UnitSelection(self, *args, **kwargs)

    def copy(self):
        return self.subgroup(self)

    def __or__(self, other: Units) -> Units:
        return Units(
            chain(
                iter(self),
                (
                    other_unit
                    for other_unit in other
                    if other_unit.tag
                    not in (self_unit.tag for self_unit in self)
                ),
            ),
            self._bot_object,
        )

    def __add__(self, other: Units) -> Units:
        return Units(
            chain(
                iter(self),
                (
                    other_unit
                    for other_unit in other
                    if other_unit.tag
                    not in (self_unit.tag for self_unit in self)
                ),
            ),
            self._bot_object,
        )

    def __and__(self, other: Units) -> Units:
        return Units(
            (
                other_unit
                for other_unit in other
                if other_unit.tag in (self_unit.tag for self_unit in self)
            ),
            self._bot_object,
        )

    def __sub__(self, other: Units) -> Units:
        return Units(
            (
                self_unit
                for self_unit in self
                if self_unit.tag
                not in (other_unit.tag for other_unit in other)
            ),
            self._bot_object,
        )

    def __hash__(self):
        return hash(unit.tag for unit in self)

    @property
    def amount(self) -> int:
        return len(self)

    @property
    def empty(self) -> bool:
        return not bool(self)

    @property
    def exists(self) -> bool:
        return bool(self)

    def find_by_tag(self, tag) -> Optional[Unit]:
        for unit in self:
            if unit.tag == tag:
                return unit
        return None

    def by_tag(self, tag):
        unit = self.find_by_tag(tag)
        if unit is None:
            raise KeyError("Unit not found")
        return unit

    @property
    def first(self) -> Unit:
        assert self, "Units object is empty"
        return self[0]

    def take(self, n: int) -> Units:
        if n >= self.amount:
            return self
        else:
            return self.subgroup(self[:n])

    @property
    def random(self) -> Unit:
        assert self, "Units object is empty"
        return random.choice(self)

    def random_or(self, other: any) -> Unit:
        return random.choice(self) if self else other

    def random_group_of(self, n: int) -> Units:
        """ Returns self if n >= self.amount. """
        if n < 1:
            return Units([], self._bot_object)
        elif n >= self.amount:
            return self
        else:
            return self.subgroup(random.sample(self, n))

    # TODO: append, insert, remove, pop and extend functions should reset the cache for Units.positions because the number of units in the list has changed
    # @property_immutable_cache
    # def positions(self) -> np.ndarray:
    #     flat_units_positions = (coord for unit in self for coord in unit.position)
    #     unit_positions_np = np.fromiter(flat_units_positions, dtype=float, count=2 * len(self)).reshape((len(self), 2))
    #     return unit_positions_np

    def in_attack_range_of(
        self, unit: Unit, bonus_distance: Union[int, float] = 0
    ) -> Units:
        """
        Filters units that are in attack range of the given unit.
        This uses the unit and target unit.radius when calculating the distance, so it should be accurate.
        Caution: This may not work well for static structures (bunker, sieged tank, planetary fortress, photon cannon, spine and spore crawler) because it seems attack ranges differ for static / immovable units.

        Example::

            enemy_zerglings = self.enemy_units(UnitTypeId.ZERGLING)
            my_marine = next((unit for unit in self.units if unit.type_id == UnitTypeId.MARINE), None)
            if my_marine:
                all_zerglings_my_marine_can_attack = enemy_zerglings.in_attack_range_of(my_marine)

        Example::

            enemy_mutalisks = self.enemy_units(UnitTypeId.MUTALISK)
            my_marauder = next((unit for unit in self.units if unit.type_id == UnitTypeId.MARAUDER), None)
            if my_marauder:
                all_mutalisks_my_marauder_can_attack = enemy_mutaliskss.in_attack_range_of(my_marauder)
                # Is empty because mutalisk are flying and marauder cannot attack air

        :param unit:
        :param bonus_distance:"""
        return self.filter(
            lambda x: unit.target_in_range(x, bonus_distance=bonus_distance)
        )

    def closest_distance_to(
        self, position: Union[Unit, Point2]
    ) -> float:
        """
        Returns the distance between the closest unit from this group to the target unit.

        Example::

            enemy_zerglings = self.enemy_units(UnitTypeId.ZERGLING)
            my_marine = next((unit for unit in self.units if unit.type_id == UnitTypeId.MARINE), None)
            if my_marine:
                closest_zergling_distance = enemy_zerglings.closest_distance_to(my_marine)
            # Contains the distance between the marine and the closest zergling

        :param position:"""
        assert self, "Units object is empty"
        if isinstance(position, Unit):
            return (
                math.sqrt(min(
                    self._bot_object._distance_squared_unit_to_unit(
                        unit, position
                    )
                    for unit in self
                ))
            )

        return math.sqrt(np.minimum(
                self._bot_object._distance_squared_units_to_pos(
                        self, position)))

    def furthest_distance_to(
        self, position: Union[Unit, Point2]
    ) -> float:
        """
        Returns the distance between the furthest unit from this group to the target unit


        Example::

            enemy_zerglings = self.enemy_units(UnitTypeId.ZERGLING)
            my_marine = next((unit for unit in self.units if unit.type_id == UnitTypeId.MARINE), None)
            if my_marine:
                furthest_zergling_distance = enemy_zerglings.furthest_distance_to(my_marine)
                # Contains the distance between the marine and the furthest away zergling

        :param position:"""
        assert self, "Units object is empty"
        if isinstance(position, Unit):
            return (
                math.sqrt(max(
                    self._bot_object._distance_squared_unit_to_unit(
                        unit, position
                    )
                    for unit in self
                ))
            )

        return math.sqrt(np.maximum(
                self._bot_object._distance_squared_units_to_pos(
                        self, position)))

    def closest_to(self, position: Union[Unit, Point2]) -> Unit:
        """
        Returns the closest unit (from this Units object) to the target unit or position.

        Example::

            enemy_zerglings = self.enemy_units(UnitTypeId.ZERGLING)
            my_marine = next((unit for unit in self.units if unit.type_id == UnitTypeId.MARINE), None)
            if my_marine:
                closest_zergling = enemy_zerglings.closest_to(my_marine)
                # Contains the zergling that is closest to the target marine

        :param position:"""
        assert self, "Units object is empty"
        if isinstance(position, Unit):
            distances = self._bot_object._distance_squared_units_to_unit(
                    self, position)
        else:
            distances = self._bot_object._distance_squared_units_to_pos(
                self, position)

        return self[distances.argmin()]

    def furthest_to(self, position: Union[Unit, Point2]) -> Unit:
        """
        Returns the furhest unit (from this Units object) to the target unit or position.

        Example::

            enemy_zerglings = self.enemy_units(UnitTypeId.ZERGLING)
            my_marine = next((unit for unit in self.units if unit.type_id == UnitTypeId.MARINE), None)
            if my_marine:
                furthest_zergling = enemy_zerglings.furthest_to(my_marine)
                # Contains the zergling that is furthest away to the target marine

        :param position:"""
        assert self, "Units object is empty"
        if isinstance(position, Unit):
            distances = self._bot_object._distance_squared_units_to_unit(
                    self, position)
        else:
            distances = self._bot_object._distance_squared_units_to_pos(
                self, position)

        return self[distances.argmax()]

    def closer_than(
        self,
        distance: Union[int, float],
        position: Union[Unit, Point2],
    ) -> Units:
        """
        Returns all units (from this Units object) that are closer than 'distance' away from target unit or position.

        Example::

            enemy_zerglings = self.enemy_units(UnitTypeId.ZERGLING)
            my_marine = next((unit for unit in self.units if unit.type_id == UnitTypeId.MARINE), None)
            if my_marine:
                close_zerglings = enemy_zerglings.closer_than(3, my_marine)
                # Contains all zerglings that are distance 3 or less away from the marine (does not include unit radius in calculation)

        :param distance:
        :param position:
        """
        if not self:
            return self
        distance_squared = distance ** 2

        if isinstance(position, Unit):
            return self.subgroup(
                unit
                for unit in self
                if self._bot_object._distance_squared_unit_to_unit(
                    unit, position
                )
                < distance_squared
            )

        distances = self._bot_object._distance_squared_units_to_pos(
                self, position)

        indices = np.nonzero(distances <= distance_squared)[0]
        return self.subgroup(self[i] for i in indices)

    def further_than(
        self,
        distance: Union[int, float],
        position: Union[Unit, Point2],
    ) -> Units:
        """
        Returns all units (from this Units object) that are further than 'distance' away from target unit or position.

        Example::

            enemy_zerglings = self.enemy_units(UnitTypeId.ZERGLING)
            my_marine = next((unit for unit in self.units if unit.type_id == UnitTypeId.MARINE), None)
            if my_marine:
                far_zerglings = enemy_zerglings.further_than(3, my_marine)
                # Contains all zerglings that are distance 3 or more away from the marine (does not include unit radius in calculation)

        :param distance:
        :param position:
        """
        if not self:
            return self
        distance_squared = distance ** 2

        if isinstance(position, Unit):
            return self.subgroup(
                unit
                for unit in self
                if self._bot_object._distance_squared_unit_to_unit(
                    unit, position
                )
                > distance_squared
            )

        distances = self._bot_object._distance_squared_units_to_pos(
                self, position)

        indices = np.nonzero(distances > distance_squared)[0]
        return self.subgroup(self[i] for i in indices)

    def in_distance_of_group(
        self, other_units: Units, distance: float
    ) -> Units:
        """Returns units that are closer than distance from any unit in the other units object.

        :param other_units:
        :param distance:
        """
        assert other_units, "Other units object is empty"
        # Return self because there are no enemies
        if not self:
            return self
        distance_squared = distance ** 2
        if len(self) == 1:
            if any(
                self._bot_object._distance_squared_unit_to_unit(
                    self[0], target
                )
                < distance_squared
                for target in other_units
            ):
                return self
            else:
                return self.subgroup([])

        return self.subgroup(
            self_unit
            for self_unit in self
            if any(
                self._bot_object._distance_squared_unit_to_unit(
                    self_unit, other_unit
                )
                < distance_squared
                for other_unit in other_units
            )
        )

    def subgroup(self, units):
        """
        Creates a new mutable Units object from Units or list object.

        :param units:"""
        return Units(units, self._bot_object)

    def filter(self, pred: callable) -> Units:
        """
        Filters the current Units object and returns a new Units object.

        Example::

            from sc2.ids.unit_typeid import UnitTypeId
            my_marines = self.units.filter(lambda unit: unit.type_id == UnitTypeId.MARINE)

            completed_structures = self.structures.filter(lambda structure: structure.is_ready)

            queens_with_energy_to_inject = self.units.filter(lambda unit: unit.type_id == UnitTypeId.QUEEN and unit.energy >= 25)

            orbitals_with_energy_to_mule = self.structures.filter(lambda structure: structure.type_id == UnitTypeId.ORBITALCOMMAND and structure.energy >= 50)

            my_units_that_can_shoot_up = self.units.filter(lambda unit: unit.can_attack_air)

        See more unit properties in unit.py

        :param pred:
        """
        assert callable(pred), "Function is not callable"
        return self.subgroup(filter(pred, self))

    def sorted(self, key: callable, reverse: bool = False) -> Units:
        return self.subgroup(sorted(self, key=key, reverse=reverse))

    def sorted_by_distance_to(
        self,
        position: Union[Unit, Point2],
        reverse: bool = False,
    ) -> Units:
        """ Returns a new Units object sorted to position (fast)"""
        if not self:
            return self

        if isinstance(position, Unit):
            return self.subgroup(
                sorted(
                    self,
                    key=lambda unit: self._bot_object._distance_squared_unit_to_unit(
                        unit, position
                    ),
                    reverse=reverse,
                )
            )

        distances = self._bot_object._distance_squared_units_to_pos(
                self, position)
        indices = distances.argsort(axis=None)
        if reverse:
            indices = indices[::-1]

        return self.subgroup(self[i] for i in indices)

    def tags_in(
        self, other: Union[Set[int], List[int], Dict[int, Any]]
    ) -> Units:
        """Filters all units that have their tags in the 'other' set/list/dict

        Example::

            my_inject_queens = self.units.tags_in(self.queen_tags_assigned_to_do_injects)

            # Do not use the following as it is slower because it first loops over all units to filter out if they are queens and loops over those again to check if their tags are in the list/set
            my_inject_queens_slow = self.units(QUEEN).tags_in(self.queen_tags_assigned_to_do_injects)

        :param other:
        """
        return self.filter(lambda unit: unit.tag in other)

    def tags_not_in(
        self, other: Union[Set[int], List[int], Dict[int, Any]]
    ) -> Units:
        """
        Filters all units that have their tags not in the 'other' set/list/dict

        Example::

            my_non_inject_queens = self.units.tags_not_in(self.queen_tags_assigned_to_do_injects)

            # Do not use the following as it is slower because it first loops over all units to filter out if they are queens and loops over those again to check if their tags are in the list/set
            my_non_inject_queens_slow = self.units(QUEEN).tags_not_in(self.queen_tags_assigned_to_do_injects)

        :param other:
        """
        return self.filter(lambda unit: unit.tag not in other)

    def of_type(
        self,
        other: Union[
            UnitTypeId,
            Set[UnitTypeId],
            List[UnitTypeId],
            Dict[UnitTypeId, Any],
        ],
    ) -> Units:
        """
        Filters all units that are of a specific type

        Example::

            # Use a set instead of lists in the argument
            some_attack_units = self.units.of_type({ZERGLING, ROACH, HYDRALISK, BROODLORD})

        :param other:"""
        if isinstance(other, UnitTypeId):
            other = {other}
        elif isinstance(other, list):
            other = set(other)
        return self.filter(lambda unit: unit.type_id in other)

    def exclude_type(
        self,
        other: Union[
            UnitTypeId,
            Set[UnitTypeId],
            List[UnitTypeId],
            Dict[UnitTypeId, Any],
        ],
    ) -> Units:
        """
        Filters all units that are not of a specific type

        Example::

            # Use a set instead of lists in the argument
            ignore_units = self.enemy_units.exclude_type({LARVA, EGG, OVERLORD})

        :param other:"""
        if isinstance(other, UnitTypeId):
            other = {other}
        elif isinstance(other, list):
            other = set(other)
        return self.filter(lambda unit: unit.type_id not in other)

    def same_tech(self, other: Set[UnitTypeId]) -> Units:
        """
        Returns all structures that have the same base structure.

        Untested: This should return the equivalents for WarpPrism, Observer, Overseer, SupplyDepot and others

        Example::

            # All command centers, flying command centers, orbital commands, flying orbital commands, planetary fortress
            terran_townhalls = self.townhalls.same_tech(UnitTypeId.COMMANDCENTER)

            # All hatcheries, lairs and hives
            zerg_townhalls = self.townhalls.same_tech({UnitTypeId.HATCHERY})

            # All spires and greater spires
            spires = self.townhalls.same_tech({UnitTypeId.SPIRE})
            # The following returns the same
            spires = self.townhalls.same_tech({UnitTypeId.GREATERSPIRE})

            # This also works with multiple unit types
            zerg_townhalls_and_spires = self.structures.same_tech({UnitTypeId.HATCHERY, UnitTypeId.SPIRE})

        :param other:
        """
        assert isinstance(other, set), (
            f"Please use a set as this filter function is already fairly slow. For example"
            + " 'self.units.same_tech({UnitTypeId.LAIR})'"
        )
        tech_alias_types: Set[int] = {u.value for u in other}
        unit_data = self._bot_object._game_data.units
        for unitType in other:
            for same in unit_data[unitType.value]._proto.tech_alias:
                tech_alias_types.add(same)
        return self.filter(
            lambda unit: unit._proto.unit_type in tech_alias_types
            or any(
                same in tech_alias_types
                for same in unit._type_data._proto.tech_alias
            )
        )

    def same_unit(
        self,
        other: Union[
            UnitTypeId,
            Set[UnitTypeId],
            List[UnitTypeId],
            Dict[UnitTypeId, Any],
        ],
    ) -> Units:
        """
        Returns all units that have the same base unit while being in different modes.

        Untested: This should return the equivalents for WarpPrism, Observer, Overseer, SupplyDepot and other units that have different modes but still act as the same unit

        Example::

            # All command centers on the ground and flying
            ccs = self.townhalls.same_unit(UnitTypeId.COMMANDCENTER)

            # All orbital commands on the ground and flying
            ocs = self.townhalls.same_unit(UnitTypeId.ORBITALCOMMAND)

            # All roaches and burrowed roaches
            roaches = self.units.same_unit(UnitTypeId.ROACH)
            # This is useful because roach has a different type id when burrowed
            burrowed_roaches = self.units(UnitTypeId.ROACHBURROWED)

        :param other:
        """
        if isinstance(other, UnitTypeId):
            other = {other}
        unit_alias_types: Set[int] = {u.value for u in other}
        unit_data = self._bot_object._game_data.units
        for unitType in other:
            unit_alias_types.add(unit_data[unitType.value]._proto.unit_alias)
        unit_alias_types.discard(0)
        return self.filter(
            lambda unit: unit._proto.unit_type in unit_alias_types
            or unit._type_data._proto.unit_alias in unit_alias_types
        )

    @property
    def center(self) -> Point2:
        """ Returns the central position of all units. """
        assert self, f"Units object is empty"
        amount = self.amount
        return Point2(
            (
                sum(unit._proto.pos.x for unit in self) / amount,
                sum(unit._proto.pos.y for unit in self) / amount,
            )
        )

    @property
    def selected(self) -> Units:
        """ Returns all units that are selected by the human player. """
        return self.filter(lambda unit: unit.is_selected)

    @property
    def tags(self) -> Set[int]:
        """ Returns all unit tags as a set. """
        return {unit.tag for unit in self}

    @property
    def ready(self) -> Units:
        """ Returns all structures that are ready (construction complete). """
        return self.filter(lambda unit: unit.is_ready)

    @property
    def not_ready(self) -> Units:
        """ Returns all structures that are not ready (construction not complete). """
        return self.filter(lambda unit: not unit.is_ready)

    @property
    def idle(self) -> Units:
        """ Returns all units or structures that are doing nothing (unit is standing still, structure is doing nothing). """
        return self.filter(lambda unit: unit.is_idle)

    @property
    def flying(self) -> Units:
        """ Returns all units that are flying. """
        return self.filter(lambda unit: unit.is_flying)

    @property
    def not_flying(self) -> Units:
        """ Returns all units that not are flying. """
        return self.filter(lambda unit: not unit.is_flying)

    @property
    def gathering(self) -> Units:
        """ Returns all workers that are mining minerals or vespene (gather command). """
        return self.filter(lambda unit: unit.is_gathering)

    @property
    def returning(self) -> Units:
        """ Returns all workers that are carrying minerals or vespene and are returning to a townhall. """
        return self.filter(lambda unit: unit.is_returning)

    @property
    def collecting(self) -> Units:
        """ Returns all workers that are mining or returning resources. """
        return self.filter(lambda unit: unit.is_collecting)

    @property
    def visible(self) -> Units:
        """Returns all units or structures that are visible.
        TODO: add proper description on which units are exactly visible (not snapshots?)"""
        return self.filter(lambda unit: unit.is_visible)

    @property
    def mineral_field(self) -> Units:
        """ Returns all units that are mineral fields. """
        return self.filter(lambda unit: unit.is_mineral_field)

    @property
    def vespene_geyser(self) -> Units:
        """ Returns all units that are vespene geysers. """
        return self.filter(lambda unit: unit.is_vespene_geyser)

    @property
    def prefer_idle(self) -> Units:
        """ Sorts units based on if they are idle. Idle units come first. """
        return self.sorted(lambda unit: unit.is_idle, reverse=True)


class UnitSelection(Units):
    def __init__(self, parent, selection=None):
        if isinstance(selection, (UnitTypeId)):
            super().__init__(
                (unit for unit in parent if unit.type_id == selection),
                parent._bot_object,
            )
        elif isinstance(selection, set):
            assert all(
                isinstance(t, UnitTypeId) for t in selection
            ), f"Not all ids in selection are of type UnitTypeId"
            super().__init__(
                (unit for unit in parent if unit.type_id in selection),
                parent._bot_object,
            )
        elif selection is None:
            super().__init__((unit for unit in parent), parent._bot_object)
        else:
            assert isinstance(
                selection, (UnitTypeId, set)
            ), f"selection is not None or of type UnitTypeId or Set[UnitTypeId]"
