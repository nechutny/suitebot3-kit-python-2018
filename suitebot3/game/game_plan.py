from typing import Dict

from suitebot3.game.point import Point

class GamePlan:

    def __init__(self,
                 width: int,
                 height: int,
                 starting_positions: Dict[int, Point],
                 max_rounds: int):
        self.width = width
        self.height = height
        self.starting_positions = starting_positions
        self.max_rounds = max_rounds

        self.validate_starting_positions()

    def validate_starting_positions(self):
        for position in self.starting_positions.values():
            self.check_is_on_plan(position)

    def check_is_on_plan(self, position: Point):
        if position.x < 0 or position.y < 0 or position.x >= self.width or position.y >= self.height:
            raise RuntimeError('Position ' + position + ' is outside of game plan')
