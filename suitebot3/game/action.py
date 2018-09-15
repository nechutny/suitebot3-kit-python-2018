from typing import Optional

from suitebot3.game.point import Point


class Action(object):
    def __init__(self, dx: int, dy: int, char: str) -> None:
        self.dx = dx
        self.dy = dy
        self.char = char

    def __str__(self) -> str:
        return self.char

    def from_point(self, point: Point) -> Point:
        return Point(point.x + self.dx, point.y + self.dy)


class Actions:
    UP = Action(0, -1, "U")
    DOWN = Action(0, 1, "D")
    LEFT = Action(-1, 0, "L")
    RIGHT = Action(1, 0, "R")
    HOLD = Action(0, 0, "H")
    PLANT_BOMB = Action(0, 0, "B")


def string_2_action(c: Optional[str]) -> Action:
    if c is None:
        return Actions.HOLD

    c = c.upper()

    if c.startswith("U"):
        return Actions.UP
    elif c.startswith("D"):
        return Actions.DOWN
    elif c.startswith("L"):
        return Actions.LEFT
    elif c.startswith("R"):
        return Actions.RIGHT
    elif c.startswith("B") or c.startswith("P"):
        return Actions.PLANT_BOMB
    else:
        return Actions.HOLD
