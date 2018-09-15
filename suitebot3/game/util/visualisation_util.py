import math

from suitebot3.game.game_constants import GameConstants


class VisualisationUtil:
    BOMB_CHARS = "0123456789"
    RESOURCES_CHARS = " ."
    BASE_CHARS = "ABCDEFGH"
    AGENT_CHARS = "abcdefgh"

    @staticmethod
    def get_resource_char(resource_count: int) -> str:
        index = len(VisualisationUtil.RESOURCES_CHARS) * resource_count / (GameConstants.FIELD_MAX_RESOURCES + 1)
        return VisualisationUtil.RESOURCES_CHARS[index]

    @staticmethod
    def get_resources(c: str) -> int:
        index = VisualisationUtil.RESOURCES_CHARS.find(c)
        return math.ceil(index * GameConstants.FIELD_MAX_RESOURCES / len(VisualisationUtil.RESOURCES_CHARS))

    @staticmethod
    def get_player_id(c: str) -> int:
        if c in VisualisationUtil.AGENT_CHARS:
            return VisualisationUtil.AGENT_CHARS.find(c) + 1
        else:
            return VisualisationUtil.BASE_CHARS.find(c) + 1
