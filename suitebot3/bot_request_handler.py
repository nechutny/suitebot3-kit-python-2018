import traceback

from suitebot3.game.dto.json_util import decode_game_state_dto
from suitebot3.game.game_setup import game_state_2_game_setup
from suitebot3.game.game_state_creator import dto_2_game_state
from suitebot3.game.moves import Moves
from suitebot3.server.simple_request_handler import SimpleRequestHandler


class BotRequestHandler(SimpleRequestHandler):
    def __init__(self, bot_ai_factory) -> None:
        '''
        :param bot_ai_factory: lambda function taking GameSetup as argument and returning BotAi
        '''
        self.bot_ai_factory = bot_ai_factory
        self.bot_ai = None

    def process_request(self, request: str) -> str:
        try:
            return self._process_request_internal(request).serialize()
        except Exception as e:
            print(e)
            traceback.print_exc()
            return str(e)

    def _process_request_internal(self, request: str) -> Moves:
        dto = decode_game_state_dto(request)

        if dto['currentRound'] == 1:
            self.bot_ai = self.bot_ai_factory(game_state_2_game_setup(dto))

        return self.bot_ai.make_moves(dto_2_game_state(dto))
