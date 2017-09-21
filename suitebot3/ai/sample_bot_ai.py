from suitebot3.ai.bot_ai import BotAi
from suitebot3.game.game_setup import GameSetup
from suitebot3.game.game_state import GameState
from suitebot3.game.moves import Moves


class SampleBotAi(BotAi):
    def __init__(self, game_setup: GameSetup):
        ''' Called before each new game '''

    def make_moves(self, game_state: GameState) -> Moves:
        return Moves()
