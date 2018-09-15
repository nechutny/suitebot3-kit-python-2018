#!/bin/bash
cd "$( dirname "${BASH_SOURCE[0]}" )"
python3 -u -m suitebot3.bot_server $*
