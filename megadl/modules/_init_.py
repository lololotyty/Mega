# Module loader for megadl
print("> Loading modules...")
# Import all module files for Pyrogram to discover them
from . import (
    admin,
    auth,
    bonus,
    callbacks,
    generals,
    mega_dl,
    mega_up
)
print("> Modules loaded successfully!") 
