import json
import unittest

from suitebot3.game.game_setup import dto_2_game_setup
from suitebot3.game.point import Point
from test_suite.test_bot_request_handler import create_game_state_string


class TestGamePlan(unittest.TestCase):

    def test_dto_2_game_setup(self):
        game_setup = dto_2_game_setup(json.loads(create_game_state_string(7)))

        self.assertEqual(game_setup.ai_player_id, 1)

        self.assertEqual(game_setup.game_plan.width, 14)
        self.assertEqual(game_setup.game_plan.height, 14)
        self.assertEqual(len(game_setup.game_plan.starting_positions), 4)
        self.assertEqual(game_setup.game_plan.starting_positions[1], Point(3, 10))
        self.assertEqual(game_setup.game_plan.starting_positions[4], Point(3, 3))
        self.assertEqual(game_setup.game_plan.max_rounds, 100)

        self.assertEqual(len(game_setup.player_ids), 4)
        self.assertTrue(1 in game_setup.player_ids)
        self.assertTrue(2 in game_setup.player_ids)
        self.assertTrue(3 in game_setup.player_ids)
        self.assertTrue(4 in game_setup.player_ids)
