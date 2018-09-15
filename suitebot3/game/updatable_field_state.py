from typing import Optional

from suitebot3.game.bomb import Bomb
from suitebot3.game.agent import Agent
from suitebot3.game.field_state import FieldState


class UpdatableFieldState(FieldState):
    def __init__(self, base: Optional[int], initial_resources: int):
        self.agent = None
        self.base = base
        self.resources = initial_resources
        self.bomb = None

        if base is not None and self.resources != 0:
            raise Exception("It is not possible to have resources where home base is")

    def get_resource_count(self) -> int:
        return self.resources

    def get_agent(self) -> Optional[Agent]:
        return self.agent

    def get_base(self) -> Optional[int]:
        return self.base

    def get_bomb(self) -> Optional[Bomb]:
        return self.bomb
