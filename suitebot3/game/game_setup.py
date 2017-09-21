from typing import Iterable, Any

from suitebot3.game.game_plan import GamePlan

class GameSetup:
    def __init__(self,
                 ai_player_id: int,
                 player_ids: Iterable[int],
                 game_plan: GamePlan):
        self.ai_player_id = ai_player_id
        self.player_ids = tuple(player_ids)
        self.game_plan = game_plan

def game_state_2_game_setup(dto: Any) -> GameSetup:
    return GameSetup(dto['aiPlayerId'], [], None)