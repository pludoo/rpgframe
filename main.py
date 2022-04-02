import rpgframe #import base Pokeframe file
from log import Log # optional import that lets you Log (only shows if debug is set to true, found in rpgframe.py file)

# creating the QuestManager object
QuestManager = rpgframe.quest.QuestManager()

# create the Player object
Player = rpgframe.player.Player("Name")

# an Item object takes 2 arguments, a name and description for it.
# For more item functionality you can create a custom class derived from
# Item and make custom functions
item1 = rpgframe.item.Item("Name", "Description")

# add/remove item from player inventory (contains 10 item slots)
Player.add_item(item1)
Player.remove_item(item1)

# a Quest object takes 4 arguments, a title, description,
# and the reward for completing (must be Item object or an object derived from Item)
quest1 = rpgframe.quest.Quest("Title", "Description", item1)

# the assign function of QuestManager takes in two arguments, 
# which quest to assign, and to who (in this case the Player).
QuestManager.assign(quest1, Player)
# You can also remove the current quest from the player
QuestManager.remove(Player)


# the NPC object takes 2 arguments, the name
# and inventory of pets (list)
# any pets that you wish to give the NPC will go into the inv argument
npc1 = rpgframe.npc.NPC("Little Kid", [])

# the NPC object has a built in talk function
npc1.talk(f"Hello, {Player.name}! I will surpass you some day!")
