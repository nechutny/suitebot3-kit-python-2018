import json
from typing import Any

''' Do not modify '''

def decode_game_state_dto(jsonStr: str) -> Any:
    return json.loads(jsonStr)
