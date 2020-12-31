from typing import Tuple, Iterable, Generator
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
    def _units_count(self) -> int:
        return len(self.all_units)

    @property
    def _cdist(self) -> np.ndarray:
        """ As property, so it will be recalculated each time it is called, or return from cache if it is called multiple times in teh same game_loop. """
        if self._generated_frame != self.state.game_loop:
            return self._calculate_distances()
        return self._cached_cdist

    def _calculate_distances(self) -> np.ndarray:
        """ Nearly same as above, but without asserts"""
        self._generated_frame = self.state.game_loop
        flat_positions = (
            coord for unit in self.all_units for coord in unit.position_tuple
        )
        positions_array: np.ndarray = np.fromiter(
            flat_positions, dtype=np.float, count=2 * self._units_count
        ).reshape((-1, 2))
        # See performance benchmarks
        self._cached_cdist = cdist(
            positions_array, positions_array, "sqeuclidean"
        )

        return self._cached_cdist

    # Helper functions

    def square_to_condensed(self, i, j) -> int:
        # Converts indices of a square matrix to condensed matrix
        # https://stackoverflow.com/a/36867493/10882657
        assert (
            i != j
        ), "No diagonal elements in condensed matrix! Diagonal elements are zero"
        if i < j:
            i, j = j, i
        return self._units_count * j - j * (j + 1) // 2 + i - 1 - j

    def convert_tuple_to_numpy_array(
        self, pos: Tuple[float, float]
    ) -> np.ndarray:
        """ Converts a single position to a 2d numpy array with 1 row and 2 columns. """
        return np.fromiter(pos, dtype=float, count=2).reshape((1, 2))

    # Fast and simple calculation functions

    def distance_math_hypot(
        self, p1: Tuple[float, float], p2: Tuple[float, float]
    ):
        return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

    def distance_math_hypot_squared(
        self, p1: Tuple[float, float], p2: Tuple[float, float]
    ):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    # Distance calculation using the pre-calculated matrix above

    def _distance_squared_unit_to_unit(
        self, unit1: Unit, unit2: Unit
    ) -> float:
        # Calculate index, needs to be after cdist has been calculated and cached
        return self._cdist[
            unit1.distance_calculation_index, unit2.distance_calculation_index
        ]

    # Distance calculation using the fastest distance calculation functions

    def _distance_pos_to_pos(
        self, pos1: Tuple[float, float], pos2: Tuple[float, float]
    ) -> float:
        return self.distance_math_hypot(pos1, pos2)

    def _distance_squared_units_to_pos(
        self, units: Units, pos: Tuple[float, float]
    ):
        """ Returns numpy array of square distances from position to units"""
        return cdist(
            [pos], [unit.position_tuple for unit in units], "sqeuclidean"
        )[0]
