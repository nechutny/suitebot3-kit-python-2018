from abc import ABCMeta, abstractmethod

from suitebot3.game.action import Action
from suitebot3.game.game_state import GameState


class BotAi:
    __metaclass__ = ABCMeta

    @abstractmethod
    def make_move(self, game_state: GameState) -> Action:
        """
        :param game_state: the current state of the game
        :return the moves to play
        """
