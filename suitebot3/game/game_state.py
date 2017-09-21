from abc import ABCMeta, abstractmethod

class GameState:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_current_round(self) -> int:
        ''

    @abstractmethod
    def get_rounds_remaining(self) -> int:
        ''