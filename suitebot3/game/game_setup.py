from typing import Iterable, Any, List

from suitebot3.game.game_plan import GamePlan
from suitebot3.game.game_state import GameState
from suitebot3.game.game_state_creator import create_player_list_from_dto, create_game_plan_from_dto


class GameSetup:
    def __init__(self,
                 ai_player_id: int,
                 player_ids: Iterable[int],
                 game_plan: GamePlan):
        self.ai_player_id = ai_player_id                                       # type: int
        self.player_ids = tuple([int(player_id) for player_id in player_ids])  # type: List[int]
        self.game_plan = game_plan                                             # type: GamePlan


def dto_2_game_setup(dto: Any) -> GameSetup:
    return GameSetup(dto['aiPlayerId'], create_player_list_from_dto(dto), create_game_plan_from_dto(dto))


def game_state_2_game_setup(ai_player_id: int, game_state: GameState) -> GameSetup:
    return GameSetup(ai_player_id, game_state.get_players(), game_state.get_game_plan())
