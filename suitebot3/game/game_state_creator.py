from typing import Any, List

from suitebot3.game.standard_game_state import StandardGameState


def string_2_game_state(game_state_as_string: str) -> StandardGameState:
    return StandardGameState(1, 10)

def dto_2_game_state(dto: Any) -> StandardGameState:
    return StandardGameState(dto['currentRound'], dto['remainingRounds'])
