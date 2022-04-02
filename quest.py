from log import Log


class Quest:
    def __init__(self, title, desc, reward):
        self.title = title
        self.desc = desc
        self.reward = reward
        self.assigned_to = None

    def print_info(self): #prints the pet inventory
        Log("Quest Info:")
        Log(self.title)
        Log(self.desc)
        Log(self.reward.name)

    def on_complete(self): # on quest complete call this function
        print(f"{self.assigned_to.name} completed {self.title}!")
        print(f'Rewarded "{self.reward.name}"!')
        self.assigned_to.item_inv.append(self.reward) # append reward to player item inv

class QuestManager:
    def __init__(self):
        Log("Initializing Quest Manager")

    def completed(self, player):
        try:
            player.current_quest.on_complete()
        except:
            Log("Player does not have a Quest currently")

    def assign(self, quest, player): # assign quest to player
        try:
            quest.assigned_to = player
            player.current_quest = quest
        except Exception as e:
            Log(f"Could not assign Player a quest: {e}")

    def remove(self, player): # in the case the player want's to cancel current quest
        try:
            player.current_quest = None
        except Exception as e:
            Log(f"Could not remove Player's current quest: {e}")

