from typing import Any

from suitebot3.game.standard_game_state import StandardGameState


def string_2_game_state(gameStateAsString: str) -> StandardGameState:
    return StandardGameState(1, 10)

def dto_2_game_state(dto: Any) -> StandardGameState:
    return StandardGameState(dto['currentRound'], dto['remainingRounds'])