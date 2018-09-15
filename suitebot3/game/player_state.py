from typing import Optional

from suitebot3.game.action import Action
from suitebot3.game.agent import Agent
from suitebot3.game.game_constants import GameConstants
from suitebot3.game.point import Point


class PlayerState:
    def __init__(self, player_id: int):
        self.agent = None                                        # type: Optional[Agent]
        self.resources = GameConstants.PLAYER_INITIAL_RESOURCES  # type: int
        self.player_id = player_id                               # type: int

    def spawn_new_agent(self, position: Point) -> Agent:
        if self.agent is not None:
            raise Exception("The player already has an agent")

        self.agent = _PlayersAgent(position, self)
        return self.agent

    def kill_agent(self):
        self.agent = None


class _PlayersAgent(Agent):
    def __init__(self,
                 position: Point,
                 player_state: PlayerState):
        self.position = position          # type: Point
        self.player_state = player_state  # type: PlayerState
        self.last_action = None           # type: Optional[Action]

    def get_player(self) -> int:
        return self.player_state.player_id

    def get_position(self) -> Point:
        return self.position

    def get_last_action(self) -> Optional[Action]:
        return self.last_action

    def kill(self):
        self.player_state.kill_agent()
