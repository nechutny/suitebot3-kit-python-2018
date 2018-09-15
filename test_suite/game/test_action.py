import unittest

from suitebot3.game.action import Actions, string_2_action
from suitebot3.game.point import Point


class TestAction(unittest.TestCase):

    def test_point_transformation(self):
        source = Point(3, 7)

        self.assertEquals(Actions.UP.from_point(source), Point(3, 6))
        self.assertEquals(Actions.DOWN.from_point(source), Point(3, 8))
        self.assertEquals(Actions.LEFT.from_point(source), Point(2, 7))
        self.assertEquals(Actions.RIGHT.from_point(source), Point(4, 7))
        self.assertEquals(Actions.HOLD.from_point(source), source)
        self.assertEquals(Actions.PLANT_BOMB.from_point(source), source)

    def test_from_string(self):
        self.assertEquals(string_2_action('U'), Actions.UP)
        self.assertEquals(string_2_action('D'), Actions.DOWN)
        self.assertEquals(string_2_action('L'), Actions.LEFT)
        self.assertEquals(string_2_action('left'), Actions.LEFT)
        self.assertEquals(string_2_action('Right'), Actions.RIGHT)
        self.assertEquals(string_2_action('H'), Actions.HOLD)
        self.assertEquals(string_2_action('B'), Actions.PLANT_BOMB)
        self.assertEquals(string_2_action('PLANT'), Actions.PLANT_BOMB)
        self.assertEquals(string_2_action(''), Actions.HOLD)
        self.assertEquals(string_2_action(' '), Actions.HOLD)
        self.assertEquals(string_2_action('None'), Actions.HOLD)

