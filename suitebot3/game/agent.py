from abc import ABCMeta, abstractmethod

from suitebot3.game.action import Action
from suitebot3.game.point import Point


class Agent:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_player(self) -> int:
        """ The player id of the owner """

    @abstractmethod
    def get_position(self) -> Point:
        """ Current position of the agent """

    def get_last_action(self) -> Action:
        """ Returns the last action the agent did or None """
