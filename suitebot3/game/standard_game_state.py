from suitebot3.game.game_state import GameState

class StandardGameState(GameState):

    def __init__(self,
                 current_round: int,
                 rounds_remaining: int):
        self.current_round = current_round
        self.rounds_remaining = rounds_remaining

    def get_current_round(self):
        return self.current_round

    def get_rounds_remaining(self):
        return self.rounds_remaining
