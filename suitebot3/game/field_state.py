from abc import ABCMeta, abstractmethod
from typing import Optional

from suitebot3.game.bomb import Bomb
from suitebot3.game.agent import Agent


class FieldState:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_resource_count(self) -> int:
        """ Get number of resources available on the field """

    @abstractmethod
    def get_agent(self) -> Optional[Agent]:
        """  Get Agent standing on the field or None """

    def get_base(self) -> Optional[int]:
        """ Get player ID of a home base located on the field or None. """

    def get_bomb(self) -> Optional[Bomb]:
        """ Get a bomb planted on the field or None. """
