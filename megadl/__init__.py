# Copyright (c) 2021 - Present Itz-fork
# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/Mega.nz-Bot
# Description: __init__.py

import os
import logging

# start msg
print("Mega.nz Bot - Cypher is starting...")


# loading config
from dotenv import load_dotenv
print("--------------------")
print("> Loading config")
if os.path.isfile('.env'):
    load_dotenv()
else:
    logging.warning("WARNING: No .env file found")

# client
from .helpers.cypher import MeganzClient
import os
# Add absolute module path for Heroku
MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
CypherClient: "MeganzClient" = MeganzClient(plugin_path=MODULE_PATH)
