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
        self.assertEquals(move, "U")

    def test_onMovesMessage_makeMoveShouldBeCalled(self):
        self.request_handler.process_request(create_game_state_string(1))
        move = self.request_handler.process_request(create_game_state_string(2))
        self.assertEquals(move, "D")

    def test_onInvalidRequest_noErrorShouldBeThrown(self):
        self.request_handler.process_request("invalid request")


def create_game_state_string(current_round: int) -> str:
    # noinspection PyPep8
    return '''
        {
            "aiPlayerId": 1,
            "currentRound": ''' + str(current_round) + ''',
            "remainingRounds": ''' + str(100 - current_round - 1) + ''',
            "gamePlanWidth": 14,
            "gamePlanHeight": 14,
            "players": {
                "1": {
                    "name": "randy 1",
                    "resources": 0,
                    "homeBaseLocation": {
                        "x": 3,
                        "y": 10
                    },
                    "agentLocation": {
                        "x": 0,
                        "y": 11
                    },
                    "agentLastMove": "UP"
                },
                "2": {
                    "name": "randy 2",
                    "resources": 0,
                    "homeBaseLocation": {
                        "x": 10,
                        "y": 3
                    },
                    "agentLocation": {
                        "x": 9,
                        "y": 4
                    },
                    "agentLastMove": "LEFT"
                },
                "3": {
                    "name": "randy 3",
                    "resources": 0,
                    "homeBaseLocation": {
                        "x": 10,
                        "y": 10
                    },
                    "agentLocation": {
                        "x": 9,
                        "y": 7
                    },
                    "agentLastMove": "LEFT"
                },
                "4": {
                    "name": "randy 4",
                    "resources": 0,
                    "homeBaseLocation": {
                        "x": 3,
                        "y": 3
                    },
                    "agentLocation": {
                        "x": 3,
                        "y": 3
                    },
                    "agentLastMove": "RIGHT"
                }
            },
            "fieldResources": [
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]
            ],
            "fieldBombs": [
                [ {"ownerId":1,"countdown":2}, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, {"ownerId":2,"countdown":4}, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ],
                [ null, null, null, null, null, null, null, null, null, null, null, null, null, null ]
            ]
        }
    '''


class DummyBotAi(BotAi):
    def make_move(self, game_state: GameState) -> Action:
        if game_state.get_current_round() == 1:
            return Actions.UP
        elif game_state.get_current_round() == 2:
            return Actions.DOWN
        else:
            raise Exception('Unexpected round ' + str(game_state.get_current_round()))

