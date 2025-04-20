# Copyright (c) 2021 - Present Itz-fork
# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/Mega.nz-Bot
# Description: __init__.py

import os
import logging
import sys

# start msg
print("Mega.nz Bot - Cypher is starting...")

# Make sure the directory is in the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.insert(0, script_dir)
print(f"> Added {script_dir} to Python path")

# loading config
from dotenv import load_dotenv
print("--------------------")
print("> Loading config")
if os.path.isfile('.env'):
    load_dotenv()
else:
    logging.warning("WARNING: No .env file found")

# Import stuff to make sure it's available
print("> Initializing modules...")
try:
    # First import client to ensure it's defined
    from .helpers.cypher import MeganzClient
    
    # Initialize client
    CypherClient: "MeganzClient" = MeganzClient()
    print("> Client initialized successfully")
except Exception as e:
    logging.error(f"Error initializing client: {e}")
