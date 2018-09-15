from typing import List, Optional, Iterator, Tuple

from suitebot3.game.agent import Agent
from suitebot3.game.bomb import Bomb
from suitebot3.game.field_state import FieldState
from suitebot3.game.game_constants import GameConstants
from suitebot3.game.game_plan import GamePlan
from suitebot3.game.game_state import GameState
from suitebot3.game.player_state import PlayerState
from suitebot3.game.point import Point
from suitebot3.game.updatable_field_state import UpdatableFieldState


class StandardGameState(GameState):

    def __init__(self,
                 game_plan: GamePlan,
                 player_ids: List[int],
                 put_agents_to_home_bases: bool = False,
                 current_round: int = 1,
                 rounds_remaining: Optional[int] = None):

        self.game_plan = game_plan
        self.players = player_ids
        self.current_round = current_round
        if rounds_remaining is None:
            self.rounds_remaining = game_plan.max_rounds - current_round + 1
        else:
            self.rounds_remaining = rounds_remaining

        self.player_state_map = {
            player_id: PlayerState(player_id)
            for player_id in self.players
        }

        ''' Access the array in this way: fields[x][y]. Or better - use method get_field(self, position: Point) '''
        self.fields = self._create_empty_fields()

        self._assert_players_unique()
        self._assert_player_ids_not_zero()
        self._assert_player_list_match_game_plan()

        if put_agents_to_home_bases:
            self.put_agents_to_home_bases()

    def get_game_plan(self) -> GamePlan:
        return self.game_plan

    def get_players(self) -> List[int]:
        return self.players

    def get_current_round(self):
        return self.current_round

    def get_rounds_remaining(self):
        return self.rounds_remaining

    def is_game_over(self) -> bool:
        return self.rounds_remaining <= 0

    def get_field(self, position: Point) -> FieldState:
        self.game_plan.check_is_on_plan(position)
        return self.fields[position.x][position.y]

    def all_fields(self) -> Iterator[Tuple[Point, FieldState]]:
        return ((position, self.get_field(position)) for position in self.game_plan)

    def get_agent_of_player(self, player_id: int) -> Optional[Agent]:
        return self.player_state_map[player_id].agent

    def get_player_resources(self, player_id: int) -> int:
        return self.player_state_map[player_id].resources

    def set_player_resources(self, player_id: int, resources: int) -> None:
        self.player_state_map[player_id].resources = resources

    def set_bomb_on_field(self, position: Point, bomb: Bomb) -> None:
        self.fields[position.x][position.y].bomb = bomb

    def set_resources_on_field(self, position: Point, resources: int) -> None:
        self.fields[position.x][position.y].resources = min(resources, GameConstants.FIELD_MAX_RESOURCES)

    def spawn_agent(self, position: Point, player_id: int) -> Agent:
        agent = self.player_state_map[player_id].spawn_new_agent(position)
        self.fields[position.x][position.y].agent = agent
        return agent

    def kill_agent(self, agent: Agent) -> None:
        x, y = agent.get_position()
        self.fields[x][y].agent = None
        self.player_state_map[agent.get_player()].kill_agent()

    def move_agent(self, agent: Agent, target_position: Point) -> None:
        source_field = self.fields[agent.get_position().x][agent.get_position().y]
        if source_field.get_agent() is agent:
            source_field.agent = None

        agent.position = target_position
        self.fields[target_position.x][target_position.y].agent = agent

    def put_agents_to_home_bases(self):
        for position, field in self.all_fields():
            if field.get_base() is not None:
                if field.get_agent() is not None:
                    raise Exception('Cannot put an agent to a home base - there is an agent already')
                self.spawn_agent(position, field.get_base())

    def _assert_players_unique(self):
        if len(set(self.players)) != len(self.players):
            raise Exception('Player ids must be unique.')

    def _assert_player_ids_not_zero(self):
        for player_id in self.players:
            if player_id == 0:
                raise Exception('Player ID cannot be 0.')

    def _assert_player_list_match_game_plan(self):
        if len(self.players) != len(self.game_plan.starting_positions):
            raise Exception('Number of players must be the same as number of starting positions on game plan.')

    def _create_empty_fields(self) -> List[List[UpdatableFieldState]]:
        fields = []

        for x in range(0, self.game_plan.width):
            fields.append([self._get_empty_field_on_position(x, y) for y in range(0, self.game_plan.height)])

        return fields

    def _get_empty_field_on_position(self, x: int, y: int) -> UpdatableFieldState:
        home_base = self._get_home_base_on_field(x, y)
        initial_resources = 0 if home_base is not None else self.game_plan.get_initial_resources()
        return UpdatableFieldState(self._get_home_base_on_field(x, y), initial_resources)

    def _get_home_base_on_field(self, x: int, y: int) -> Optional[int]:
        for player, position in self.game_plan.starting_positions.items():
            if position.x == x and position.y == y:
                return player
        return None
