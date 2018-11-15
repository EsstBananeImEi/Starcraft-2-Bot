"""
created at 15.11.2018
      time 20:56
@author: zydra
"""

import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer

class StarcraftTwoBot(sc2.BotAI):
    async def on_step(self, iteration):
        await self.distribute_workers() # intelligente verteilung die arbeiter

run_game(maps.get("AbyssalReefLE"), [
    Bot(Race.Zerg, StarcraftTwoBot()),
    Computer(Race.Terran, Difficulty.Easy)
], realtime=True)