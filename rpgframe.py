from settings import Settings
import player
import quest
import item
import npc


"""
Made by Pludo, 2021 - MIT License

** Python 3.10.1 **

RPGFrame is a framework to establish RPG type games, as of now
features include's these systems:
Player & NPC System
Questing System
Inventory Management
Logging
-- A few extra notes -- 
Items' only contain a couple variables, a name and description. To create custom items that have custom functions,
make a new class that is derived from Item in item.py or create a standalone class entirely

If the debug option in the below arguments is set to false (0), all things that are considered "debugging" will not be printed to the console.
"""
settings = Settings(debug=1)
