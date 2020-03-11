import time

from sc2.data import ActionResult, Alert, Race, Result, Target, Difficulty
# from sc2.constants import race_gas, race_townhalls, race_worker
from sc2.client import Client
from sc2.game_data import GameData
from sc2.game_info import GameInfo
from sc2.game_state import GameState

from sc2.main import run_game
from sc2.player import Bot, Computer
from sc2.maps import get as maps_get


# TODO unit type id etc
from sc2.ids.ability_id import AbilityId

from sc2.ids_updater import IdUpdater



class IdGeneratorBot:
    def __init__(self):
        pass

    async def on_step(self, iteration: int):
        """ Leave after on_start is complete. """
        await self._client.debug_leave()

    async def on_start(self):
        """ Executed before on_step, update the ids. """
        updater = IdUpdater()
        updater.update_and_reimport_ids()


    def _initialize_variables(self):
        pass

    def _prepare_start(self, client, player_id, game_info, game_data, realtime: bool = False):
        self._client: Client = client
        self.player_id: int = player_id
        self._game_info: GameInfo = game_info
        self._game_data: GameData = game_data
        self.realtime: bool = realtime

        self.race: Race = Race(self._game_info.player_races[self.player_id])

    def _prepare_first_step(self):
        pass

    def _prepare_step(self, state, proto_game_info):
        self.state: GameState = state

    async def _after_step(self):
        pass

    async def on_before_start(self):
        pass

    async def on_end(self, game_result: Result):
        pass

    async def issue_events(self):
        pass


def main():
    run_game(
        maps_get("AcropolisLE"),
        [Bot(Race.Terran, IdGeneratorBot()), Computer(Race.Zerg, Difficulty.VeryHard)],
        realtime=False,
        # Generate IDs for a specific sc2 version, see sc2.versions.py
        sc2_version="4.5.1",
    )


if __name__ == "__main__":
    main()
