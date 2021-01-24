from itertools import chain
from typing import Tuple
import warnings

import math
import numpy as np

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from scipy.spatial.distance import cdist

from loguru import logger

from sc2.position import Point2
from sc2.unit import Unit
from sc2.units import Units
from sc2.game_state import GameState


class DistanceCalculation:
    def __init__(self):
        self.state: GameState = None
        self._generated_frame = -100

        self._cached_cdist: np.ndarray = None

    @property
    def _cdist(self) -> np.ndarray:
        """ As property, so it will be recalculated each time it is called,
        or return from cache if it is called multiple times in the same game_loop. """
        if self._generated_frame != self.state.game_loop:
            return self._calculate_distances()
        return self._cached_cdist

    def _calculate_distances(self) -> np.ndarray:
        self._generated_frame = self.state.game_loop
        flat_positions = chain.from_iterable(
                unit.position_tuple for unit in self.all_units)
        positions_array: np.ndarray = np.fromiter(
            flat_positions, dtype=np.float, count=2 * len(self.all_units)
        ).reshape((-1, 2))
        # See performance benchmarks
        self._cached_cdist = cdist(
            positions_array, positions_array, "sqeuclidean"
        )

        return self._cached_cdist

    # Fast and simple calculation functions

    def distance_math_hypot(
        self, p1: Tuple[float, float], p2: Tuple[float, float]
    ):
        return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

    def distance_math_hypot_squared(
        self, p1: Tuple[float, float], p2: Tuple[float, float]
    ):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def _distance_pos_to_pos(
        self, pos1: Tuple[float, float], pos2: Tuple[float, float]
    ) -> float:
        return self.distance_math_hypot(pos1, pos2)

    # Distance calculation using the pre-calculated matrix above

    def _distance_squared_unit_to_unit(
        self, unit1: Unit, unit2: Unit
    ) -> float:
        # Calculate index, needs to be after cdist has been calculated and cached
        return self._cdist[
            unit1.distance_calculation_index, unit2.distance_calculation_index
        ]

    def _distance_squared_units_to_unit(
            self, units: Units, unit: Unit
    ) -> np.array:
        indices = np.fromiter(
                (u.distance_calculation_index for u in units),
                dtype=np.int,
                count=len(units))
        return self._cdist[indices, unit.distance_calculation_index]

    # Distance calculation using cdist

    def _distance_squared_units_to_pos(
        self, units: Units, pos: Tuple[float, float]
    ):
        """List of square distances from position to units"""
        flat_positions = chain.from_iterable(
                unit.position_tuple for unit in units)
        positions = np.fromiter(
                flat_positions,
                dtype=float,
                count=len(units) * 2)
        positions = positions.reshape((-1, 2))
        return cdist(positions, [pos], "sqeuclidean")
