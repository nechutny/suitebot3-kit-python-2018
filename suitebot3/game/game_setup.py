from typing import Iterable, Any, List

from suitebot3.game.game_plan import GamePlan

class GameSetup:
    def __init__(self,
                 ai_player_id: int,
                 player_ids: Iterable[int],
                 game_plan: GamePlan):
        self.ai_player_id = ai_player_id                                       # type: int
        self.player_ids = tuple([int(player_id) for player_id in player_ids])  # type: List[int]
        self.game_plan = game_plan                                             # type: GamePlan


def dto_2_game_setup(dto: Any) -> GameSetup:
    return GameSetup(dto['aiPlayerId'], [], None)

