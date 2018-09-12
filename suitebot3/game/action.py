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
    HOLD = Action(0, 0, "H")


def string_2_action(c: Optional[str]) -> Action:
    return Actions.HOLD
