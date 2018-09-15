
class Bomb:
    def __init__(self, owner: int, countdown: int):
        self.owner = owner  # type: int

        '''
            Number of rounds remaining before the bomb explodes.
            The bomb explodes in the round in which the countdown is 0.
            During round evaluation all agent move and then bombs explode
            so when countdown is 0 your agent have still one move to make.
        '''
        self.countdown = countdown  # type: int
