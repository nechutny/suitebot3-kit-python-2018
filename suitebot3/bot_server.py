import sys
from typing import List

from suitebot3.ai.bot_ai import BotAi
from suitebot3.ai.sample_bot_ai import SampleBotAi
from suitebot3.bot_request_handler import BotRequestHandler
from suitebot3.game.game_setup import GameSetup
from suitebot3.server.simple_server import SimpleServer

DEFAULT_PORT = 9001


def _determine_port(args: List[str]) -> int:
    if len(args) == 1:
        return int(args[0])
    else:
        return DEFAULT_PORT


def bot_ai_factory(game_setup: GameSetup) -> BotAi:
    return SampleBotAi(game_setup)  # replace with your own AI


if __name__ == "__main__":
    port = _determine_port(sys.argv[1:])

    print("listening on port %i" % port)
    SimpleServer(port, BotRequestHandler(bot_ai_factory)).run()
