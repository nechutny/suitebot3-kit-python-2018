import json
import unittest

from suitebot3.game.action import Action, Actions
from suitebot3.ai.bot_ai import BotAi
from suitebot3.bot_request_handler import BotRequestHandler
from suitebot3.game.game_state import GameState


class TestSimpleServer(unittest.TestCase):

    def setUp(self):
        self.request_handler = BotRequestHandler(lambda game_setup: DummyBotAi())
        super().setUp()

    def test_onSetupMessage_initializeShouldBeCalled(self):
        move = self.request_handler.process_request(create_game_state_string(1))
        self.assertEquals(move, "H")

    def test_onMovesMessage_makeMoveShouldBeCalled(self):
        self.request_handler.process_request(create_game_state_string(1))
        move = self.request_handler.process_request(create_game_state_string(2))
        self.assertEquals(move, "H")

    def test_onInvalidRequest_noErrorShouldBeThrown(self):
        self.request_handler.process_request("invalid request")

def create_game_state_string(currentRound: int) -> str:
    dto = {
        'currentRound': currentRound,
        'remainingRounds': 150 - currentRound,
        'aiPlayerId': 1
    }

    return json.dumps(dto)

class DummyBotAi(BotAi):
    def make_move(self, game_state: GameState) -> Action:
        if game_state.get_current_round() == 1:
            return Actions.HOLD
        elif game_state.get_current_round() == 2:
            return Actions.HOLD
        else:
            raise Exception('Unexpected round ' + str(game_state.get_current_round()))

