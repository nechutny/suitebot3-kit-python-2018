import unittest

from suitebot3.game.point import Point
from suitebot3.game.player_state import PlayerState


class TestPlayerState(unittest.TestCase):

    def setUp(self):
        super().setUp()

        self.player_state = PlayerState(1)
        self.player_state.spawn_new_agent(Point(1, 2))

    def test_get_agent(self):
        self.assertEquals(self.player_state.agent.get_position(), Point(1, 2))

    def test_kill_agent(self):
        self.player_state.kill_agent()
        self.assertIsNone(self.player_state.agent)

    def test_get_player(self):
        self.assertEquals(self.player_state.player_id, 1)
        self.assertEquals(self.player_state.agent.get_player(), 1)
