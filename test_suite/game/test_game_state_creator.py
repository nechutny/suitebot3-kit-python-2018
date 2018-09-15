import json
import unittest

from suitebot3.game.game_state_creator import string_2_game_state, dto_2_game_state
from suitebot3.game.point import Point
from test_suite.test_bot_request_handler import create_game_state_string


class TestGameStateCreator(unittest.TestCase):

    def test_creating_from_valid_string(self):
        game_state = string_2_game_state(" A \n"
                                         "B  \n")

        self.assertEquals(game_state.game_plan.width, 3)
        self.assertEquals(game_state.game_plan.height, 2)

        self.assertEquals(game_state.get_field(Point(2, 0)).get_agent(), None)
        self.assertEquals(game_state.get_field(Point(1, 1)).get_agent(), None)
        self.assertEquals(game_state.get_field(Point(1, 0)).get_agent().get_player(), 1)

        self.assertEquals(len(game_state.get_players()), 2)
        self.assertEquals(game_state.get_agent_of_player(1).get_position(), Point(1, 0))
        self.assertEquals(game_state.get_agent_of_player(2).get_position(), Point(0, 1))

    def test_invalid_character_should_throw(self):
        self.assertRaises(Exception, string_2_game_state, ' A&')

    def test_non_rectangular_throws(self):
        self.assertRaises(Exception, string_2_game_state, '  \n   \n')

    def test_from_dto(self):
        game_state = dto_2_game_state(json.loads(create_game_state_string(5)))

        self.assertEqual(game_state.current_round, 5)
        self.assertEqual(game_state.rounds_remaining, 94)

        self.assertEqual(game_state.get_field(Point(0, 0)).get_resource_count(), 1)
        self.assertEqual(game_state.get_field(Point(3, 10)).get_resource_count(), 0)
        self.assertEqual(game_state.get_field(Point(3, 10)).get_base(), 1)
        self.assertEqual(game_state.get_field(Point(0, 11)).get_agent().get_player(), 1)

        self.assertEqual(game_state.get_agent_of_player(1).get_position(), Point(0, 11))

        bomb_0_0 = game_state.get_field(Point(0, 0)).get_bomb()
        self.assertIsNotNone(bomb_0_0)
        self.assertEqual(bomb_0_0.countdown, 2)
        self.assertEqual(bomb_0_0.owner, 1)
        self.assertIsNone(game_state.get_field(Point(1, 0)).get_bomb())

        self.assertEqual(game_state.game_plan.width, 14)
        self.assertEqual(game_state.game_plan.height, 14)



