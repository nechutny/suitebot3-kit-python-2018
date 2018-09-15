import unittest

from suitebot3.game.game_setup import game_state_2_game_setup
from suitebot3.ai.sample_bot_ai import SampleBotAi
from suitebot3.game.action import Action, Actions
from suitebot3.game.game_state_creator import string_2_game_state


class TestSimpleServer(unittest.TestCase):

    PLAYER_ID = 1
    ACTIONS = [Actions.UP, Actions.DOWN, Actions.LEFT, Actions.RIGHT, Actions.PLANT_BOMB]

    def test_returns_an_action(self):
        action = self.get_action('A...')
        self.assertIn(action, self.ACTIONS)

    def get_action(self, game_state_str: str) -> Action:
        self.game_state = string_2_game_state(game_state_str)
        game_setup = game_state_2_game_setup(self.PLAYER_ID, self.game_state)
        self.action = SampleBotAi(game_setup).make_move(self.game_state)
        return self.action