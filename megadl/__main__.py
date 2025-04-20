# Copyright (c) 2021 - Present Itz-fork
# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/Mega.nz-Bot
# Description: __main__.py

import logging
import os
import sys
from pyrogram import idle

# Set up logging
logging.basicConfig(level=logging.INFO)
logging.info("Starting Mega.nz Bot...")

# Add debug info
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

try:
    # Debug module imports
    print("Importing CypherClient...")
    from . import CypherClient
    print("CypherClient imported successfully")
    
    # Import plugins manually to ensure they're loaded
    print("Manually importing plugins...")
    import megadl.modules.mega_dl
    import megadl.modules.mega_up
    import megadl.modules.generals
    import megadl.modules.callbacks
    import megadl.modules.bonus
    import megadl.modules.auth
    import megadl.modules.admin
    print("Plugins imported successfully")
    
    # Run the bot
    if __name__ == "__main__":
        # Custom pyrogram client
        print("> Starting Client")
        CypherClient.start()
        print("--------------------")
        print("> Bot is running! Send /start to begin.")
        idle()
except Exception as e:
    print(f"Error starting bot: {e}")
    import traceback
    traceback.print_exc()
