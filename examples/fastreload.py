from importlib import reload
import argparse

import sys
import asyncio

import sc2
from sc2 import Race, Difficulty
from sc2.player import Bot, Computer

from zerg import zerg_rush


def main():
    player_config = [Bot(Race.Zerg, zerg_rush.ZergRushBot()), Computer(Race.Terran, Difficulty.Medium)]

    gen = sc2.main._host_game_iter(sc2.maps.get("SubmarineLE"), player_config, realtime=False)

    r = next(gen)
    while True:
        input("Press enter to reload ")

        reload(zerg_rush)
        player_config[0].ai = zerg_rush.ZergRushBot()
        gen.send(player_config)


if __name__ == "__main__":
    main()
