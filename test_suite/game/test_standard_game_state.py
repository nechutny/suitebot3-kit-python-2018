import unittest

from suitebot3.game.game_constants import GameConstants
from suitebot3.game.game_plan import GamePlan
from suitebot3.game.point import Point
from suitebot3.game.standard_game_state import StandardGameState
from suitebot3.game.game_state_creator import string_2_game_state


class TestStandardGameState(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.game_state = string_2_game_state(".  A  \n"
                                              "      \n"
                                              "  B   \n")

    def test_mismatch_starting_positions(self):
        self.assertRaises(Exception, StandardGameState, GamePlan(10, 10, {1: Point(1, 1)}, 5), [1, 2])

    def test_get_players(self):
        self.assertEquals(set(self.game_state.get_players()), {1, 2})

    def test_empty_field(self):
        field = self.game_state.get_field(Point(0, 0))
        self.assertIsNone(field.get_agent())
        self.assertIsNone(field.get_base())
        self.assertGreater(field.get_resource_count(), 0)

    def test_field_with_agent(self):
        field = self.game_state.get_field(Point(3, 0))

        self.assertEquals(field.get_agent().get_player(), 1)
        self.assertEquals(field.get_agent().get_position(), Point(3, 0))
        self.assertEquals(field.get_agent().get_last_action(), None)

        self.assertIsNotNone(field.get_base())
        self.assertEqual(field.get_resource_count(), 0)

    def test_field_with_base(self):
        self.assertEquals(self.game_state.get_field(Point(2, 2)).get_base(), 2)

    def test_player_state_initialized(self):
        self.assertIsNotNone(self.game_state.get_agent_of_player(1))
        self.assertIsNotNone(self.game_state.get_agent_of_player(2))

    def test_spawn_agent(self):
        self.game_state.kill_agent(self.game_state.get_agent_of_player(2))
        self.game_state.spawn_agent(Point(1, 1), 2)
        self.assertEqual(self.game_state.get_agent_of_player(2).get_position(), Point(1, 1))
        self.assertEqual(self.game_state.get_field(Point(1, 1)).get_agent().get_player(), 2)

    def test_killing_agent(self):
        killed_pos = self.game_state.get_agent_of_player(1).get_position()

        self.game_state.kill_agent(self.game_state.get_agent_of_player(1))
        self.assertIsNone(self.game_state.get_field(killed_pos).get_agent())
        self.assertIsNone(self.game_state.get_agent_of_player(1))

    def test_moving_agent(self):
        agent = self.game_state.get_field(Point(2, 2)).get_agent()
        self.game_state.move_agent(agent, Point(3, 2))

        self.assertEqual(agent.get_position(), Point(3, 2))
        self.assertIsNone(self.game_state.get_field(Point(2, 2)).get_agent())
        self.assertEquals(self.game_state.get_field(Point(3, 2)).get_agent(), agent)

    def test_set_resources(self):
        self.game_state.set_player_resources(1, 1000)
        self.assertEquals(self.game_state.get_player_resources(1), 1000)

    def test_set_resources_on_field(self):
        self.game_state.set_resources_on_field(Point(2, 2), 0)
        self.assertEquals(self.game_state.get_field(Point(2, 2)).get_resource_count(), 0)

    def test_setting_more_resources_than_allowed(self):
        self.game_state.set_resources_on_field(Point(2, 2), 200000)
        self.assertEquals(self.game_state.get_field(Point(2, 2)).get_resource_count(), GameConstants.FIELD_MAX_RESOURCES)
