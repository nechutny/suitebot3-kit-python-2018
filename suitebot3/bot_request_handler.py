import json
import traceback
from typing import Any

from suitebot3.game.action import Action
from suitebot3.game.game_setup import dto_2_game_setup
from suitebot3.game.game_state_creator import dto_2_game_state
from suitebot3.server.simple_request_handler import SimpleRequestHandler


class BotRequestHandler(SimpleRequestHandler):
    def __init__(self, bot_ai_factory) -> None:
        """
        :param bot_ai_factory: lambda function taking GameSetup as argument and returning BotAi
        """
        self.bot_ai_factory = bot_ai_factory
        self.bot_ai = None

    def process_request(self, request: str) -> str:
        try:
            dto = json.loads(request)
            return str(self._process_request_internal(dto))
        except ValueError:
            return 'Invalid request - cannot parse JSON'
        except Exception as e:
            print(e)
            traceback.print_exc()
            return str(e)

    def _process_request_internal(self, dto: Any) -> Action:

        if dto['currentRound'] == 1:
            self.bot_ai = self.bot_ai_factory(dto_2_game_setup(dto))

        return self.bot_ai.make_move(dto_2_game_state(dto))
