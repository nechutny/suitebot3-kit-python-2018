from typing import Dict, Iterator

from suitebot3.game.game_constants import GameConstants
from suitebot3.game.point import Point


class GamePlan:

    def __init__(self,
                 width: int,
                 height: int,
                 starting_positions: Dict[int, Point],
                 max_rounds: int):
        self.width = width                            # type: int
        self.height = height                          # type: int
        self.starting_positions = starting_positions  # type: Dict[int, Point]
        self.max_rounds = max_rounds                  # type: int

        self.validate_starting_positions()

    def validate_starting_positions(self):
        for position in self.starting_positions.values():
            self.check_is_on_plan(position)

    def check_is_on_plan(self, position: Point):
        if position.x < 0 or position.y < 0 or position.x >= self.width or position.y >= self.height:
            raise RuntimeError('Position ' + str(position) + ' is outside of game plan')

    def __iter__(self) -> Iterator[Point]:
        """ Iterate over all fields on the game plan """
        return (Point(i // self.height, i % self.height) for i in range(0, self.width * self.height))

    @staticmethod
    def get_initial_resources():
        return GameConstants.FIELD_INITIAL_RESOURCES
