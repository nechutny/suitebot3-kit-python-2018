from abc import ABCMeta, abstractmethod
from typing import List, Optional

from suitebot3.game.agent import Agent
from suitebot3.game.bomb import Bomb
from suitebot3.game.field_state import FieldState
from suitebot3.game.game_plan import GamePlan
from suitebot3.game.point import Point


class GameState:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_game_plan(self) -> GamePlan: pass

    @abstractmethod
    def is_game_over(self) -> bool: pass

    @abstractmethod
    def get_current_round(self) -> int: pass

    @abstractmethod
    def get_rounds_remaining(self) -> int: pass

    @abstractmethod
    def get_players(self) -> List[int]: pass

    @abstractmethod
    def get_agent_of_player(self, player_id: int) -> Optional[Agent]: pass

    @abstractmethod
    def get_player_resources(self, player_id: int) -> int: pass

    @abstractmethod
    def set_player_resources(self, player_id: int, resources: int) -> None: pass

    @abstractmethod
    def spawn_agent(self, position: Point, player_id: int) -> Agent: pass

    @abstractmethod
    def kill_agent(self, agent: Agent) -> None: pass

    @abstractmethod
    def move_agent(self, agent: Agent, target_position: Point) -> None: pass

    @abstractmethod
    def get_field(self, position: Point) -> FieldState: pass

    @abstractmethod
    def set_resources_on_field(self, position: Point, resources: int) -> None: pass

    @abstractmethod
    def set_bomb_on_field(self, position: Point, bomb: Bomb) -> None: pass
