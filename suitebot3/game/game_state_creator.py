from typing import Any, List

from suitebot3.game.action import string_2_action
from suitebot3.game.bomb import Bomb
from suitebot3.game.game_plan import GamePlan
from suitebot3.game.point import Point
from suitebot3.game.standard_game_state import StandardGameState
from suitebot3.game.util.visualisation_util import VisualisationUtil

DEFAULT_MAX_ROUNDS = 150


def string_2_game_state(game_state_as_string: str) -> StandardGameState:
    """
        Creates a game state from a string representation.
        See VisualisationUtil.java for description of all available characters.
        In general:
        - Capital letters A-H are locations of home bases. Agents are placed on the home bases.
        - Characters " ." are fields with different number of resources on it.
           ' '  has 0 resources,
           '.'  has 1 resource
          - Numbers 1-9 are bombs belonging to player A with countdown equal to the number.
            There are 0 resources under a bomb.

        For example the following will create 5x5 game plan.
        There will be:
         - 1 agent of player 1 (letter 'A')
         - 1 agent of player 2 in the home base 'B'
         - resources in the upper left corner and along the bottom
         - bomb with countdown 2 in the center belonging to player A
        "...  \n" +
        ".A   \n" +
        "  2  \n" +
        "  B  \n" +
        ".....\n" +
    """
    
    lines = game_state_as_string.splitlines()

    height = len(lines)
    width = len(lines[0])

    players = []
    starting_positions = {}

    for line in lines:
        if len(line) != width:
            raise Exception('String is not rectangular - all lines must have the same length.')

    for x in range(0, width):
        for y in range(0, height):
            c = lines[y][x]

            if c in VisualisationUtil.BASE_CHARS:
                player_id = VisualisationUtil.get_player_id(c)
                players.append(player_id)
                starting_positions[player_id] = Point(x, y)
            elif c not in VisualisationUtil.AGENT_CHARS and c not in VisualisationUtil.RESOURCES_CHARS and c not in VisualisationUtil.BOMB_CHARS:
                raise Exception("Unknown character '" + c + "'")

    game_plan = GamePlan(width, height, starting_positions, DEFAULT_MAX_ROUNDS)
    game_state = StandardGameState(game_plan, players, True)

    for position, field in game_state.all_fields():
        c = lines[position.y][position.x]

        if c in VisualisationUtil.AGENT_CHARS:
            game_state.spawn_agent(position, VisualisationUtil.get_player_id(c))
            game_state.set_resources_on_field(position, 0)
        elif c in VisualisationUtil.RESOURCES_CHARS:
            game_state.set_resources_on_field(position, VisualisationUtil.get_resources(c))
        elif c in VisualisationUtil.BOMB_CHARS:
            player_id = VisualisationUtil.get_player_id('a')
            bomb = Bomb(player_id, int(c))
            game_state.set_bomb_on_field(position, bomb)
            game_state.set_resources_on_field(position, 0)
        elif c not in VisualisationUtil.BASE_CHARS:
            raise Exception("Unknown character '" + c + "'")

    return game_state


def dto_2_game_state(dto: Any) -> StandardGameState:
    players = create_player_list_from_dto(dto)
    game_plan = create_game_plan_from_dto(dto)

    game_state = StandardGameState(game_plan, players, False, dto["currentRound"], dto["remainingRounds"])

    for player_id_str, playerDto in dto["players"].items():
        player_id = int(player_id_str)
        agent_location_dto = playerDto["agentLocation"]
        agent_last_move = playerDto["agentLastMove"] if "agentLastMove" in playerDto else None

        if agent_location_dto is not None:
            agent_location = Point(agent_location_dto["x"], agent_location_dto["y"])
            agent = game_state.spawn_agent(agent_location, player_id)
            agent.last_move = string_2_action(agent_last_move)

        game_state.set_player_resources(player_id, playerDto["resources"])

    for position, field in game_state.all_fields():
        game_state.set_resources_on_field(position, dto["fieldResources"][position.x][position.y])

        bomb_dto = dto["fieldBombs"][position.x][position.y]
        if bomb_dto is not None:
            game_state.set_bomb_on_field(position, Bomb(bomb_dto["ownerId"], bomb_dto["countdown"]))

    return game_state


def create_player_list_from_dto(dto: Any) -> List[int]:
    return [int(player_id_str) for player_id_str in dto["players"].keys()]


def create_game_plan_from_dto(dto: Any) -> GamePlan:
    starting_positions = {
        int(player): Point(playerDto["homeBaseLocation"]["x"], playerDto["homeBaseLocation"]["y"]) for
        player, playerDto in dto["players"].items()}

    return GamePlan(width=dto["gamePlanWidth"],
                    height=dto["gamePlanHeight"],
                    starting_positions=starting_positions,
                    max_rounds=dto["remainingRounds"] + dto["currentRound"] + 1)
