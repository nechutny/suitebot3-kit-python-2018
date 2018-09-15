import random
from typing import NamedTuple

from suitebot3.game.action import Actions, Action
from suitebot3.ai.bot_ai import BotAi
from suitebot3.game.game_setup import GameSetup
from suitebot3.game.game_state import GameState


class SampleBotAi(BotAi):
    ACTIONS = [
        Actions.UP, Actions.DOWN, Actions.LEFT, Actions.RIGHT,
        Actions.UP, Actions.LEFT, Actions.UP, Actions.LEFT,
        Actions.PLANT_BOMB
    ]

    def __init__(self, game_setup: GameSetup):
        """ Called before each new game """
        self.my_id = game_setup.ai_player_id
        self.gameRound = 0
        self.direction = 1

    def getBestDirection(self, game_state):
        x = [1, -1]
        y = [-1, 1]

        bestDirection = 1
        bestPoints = 0

        myPosition = self.agent.get_position()

        point = NamedTuple('Point', [('x', int), ('y', int)])

        points = self.calculatePoints(game_state, myPosition.x + 2, myPosition.y - 2)
        point.x = myPosition.x + 1
        point.y = myPosition.y - 1
        points = points - game_state.get_field(point).get_resource_count()
        if points > bestPoints:
            bestDirection = 1
            bestPoints = points

        points = self.calculatePoints(game_state, myPosition.x - 2, myPosition.y - 2)
        point.x = myPosition.x - 1
        point.y = myPosition.y - 1
        points = points - game_state.get_field(point).get_resource_count()
        if points > bestPoints:
            bestDirection = 2
            bestPoints = points

        points = self.calculatePoints(game_state, myPosition.x - 2, myPosition.y + 2)
        point.x = myPosition.x - 1
        point.y = myPosition.y + 1
        points = points - game_state.get_field(point).get_resource_count()
        if points > bestPoints:
            bestDirection = 3
            bestPoints = points

        points = self.calculatePoints(game_state, myPosition.x + 2, myPosition.y + 2)
        point.x = myPosition.x + 1
        point.y = myPosition.y + 1
        points = points - game_state.get_field(point).get_resource_count()
        if points > bestPoints:
            bestDirection = 4
            bestPoints = points

        return bestDirection

    def calculatePoints(self, game_state, x, y):
        pointsum = 0
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                point = NamedTuple('Point', [('x', int), ('y', int)])
                point.x = x + i
                point.y = y + j
                pointsum = pointsum + game_state.get_field(point).get_resource_count()

        return pointsum

    def translateDirection(self, direction, state):
        if state == 1:
            if direction > 2:
                return Actions.DOWN
            else:
                return Actions.UP
        elif state == 2:
            if direction == 2 or direction == 3:
                return Actions.LEFT
            else:
                return Actions.RIGHT

    def getOccupyPercent(self, game_state: GameState):
        free = 0
        points = 0
        fields = 0
        point = NamedTuple('Point', [('x', int), ('y', int)])
        for y in range(0, game_state.get_game_plan().height):
            point.y = y
            for x in range(0, game_state.get_game_plan().width):
                point.x = x
                field = game_state.get_field(point)
                fields = fields + 1
                if field.get_resource_count() == 0:
                    free = free + 1
                else:
                    points = points + 1

        return points/fields

    def harvesAI(self, game_state):
        if self.gameRound % 5 == 0:
            self.gameRound = self.gameRound + 1
            return Actions.PLANT_BOMB
        elif self.gameRound % 5 == 1:
            self.direction = self.getBestDirection(game_state)
            self.gameRound = self.gameRound + 1
            return self.translateDirection(self.direction, 1)
        elif self.gameRound % 5 == 2:
            self.gameRound = self.gameRound + 1
            return self.translateDirection(self.direction, 1)
        elif self.gameRound % 5 == 3:
            # znovu zkontrolovat

            myPosition = self.agent.get_position()

            point = NamedTuple('Point', [('x', int), ('y', int)])

            points_right = self.calculatePoints(game_state, myPosition.x + 2, myPosition.y)
            point.x = myPosition.x + 1
            point.y = myPosition.y + ( +1 if self.translateDirection(self.direction, 1) == Actions.UP else -1)
            points_right = points_right - game_state.get_field(point).get_resource_count()

            points_left = self.calculatePoints(game_state, myPosition.x - 2, myPosition.y)
            point.x = myPosition.x - 1
            point.y = myPosition.y + (+1 if self.translateDirection(self.direction, 1) == Actions.UP else -1)
            points_left = points_left - game_state.get_field(point).get_resource_count()

            if points_left < points_right:
                self.direction = 1
            else:
                self.direction = 2

            self.gameRound = self.gameRound + 1
            return self.translateDirection(self.direction, 2)
        elif self.gameRound % 5 == 4:
            self.gameRound = self.gameRound + 1
            return self.translateDirection(self.direction, 2)

    def suicideAI(self, game_state: GameState):
        if self.gameRound%3 == 0:
            self.gameRound = self.gameRound + 1
            return Actions.PLANT_BOMB
        else:
            self.gameRound = self.gameRound + 1
            return random.choice([Actions.UP, Actions.DOWN, Actions.LEFT, Actions.RIGHT])


    def make_move(self, game_state: GameState) -> Action:
        self.agent = game_state.get_agent_of_player(self.my_id)
        try:

            if self.getOccupyPercent(game_state) > 0.05:
                return self.harvesAI(game_state)
            else:
                return self.suicideAI(game_state)


        except Exception as e:
            print(e.__doc__)
            print(str(e))
            pass

        self.gameRound = self.gameRound + 1
        return Actions.HOLD
