from suitebot3.game.action import Actions, Action
from suitebot3.ai.bot_ai import BotAi
from suitebot3.game.game_setup import GameSetup
from suitebot3.game.game_state import GameState


class SampleBotAi(BotAi):
    def __init__(self, game_setup: GameSetup):
        """ Called before each new game """
        self.my_id = game_setup.ai_player_id

    def make_move(self, game_state: GameState) -> Action:
        return Actions.HOLD
