from abc import ABCMeta, abstractmethod

from suitebot3.game.game_state import GameState
from suitebot3.game.moves import Moves


class BotAi:
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_moves(self, game_state: GameState) -> Moves:
        """
        :param gameState - the current state of the game
        :return the moves to play
        """