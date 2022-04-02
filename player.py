from log import Log


class Player:
    def __init__(self, name):
        self.name = name
        self.item_inv = [None] * 10
        self.current_quest = None

    def add_item(self, item): #add item to inventory
        if (len(self.item_inv) <= 10):
            for i in range(len(self.item_inv)): #iterate through item inventory
                if self.item_inv[i] == None: #dynamically assign item to first None type slot
                    self.item_inv[i] = item # assign item to slot
                    break # break out of loop
        else:
            Log("Player's Item inventory is full")

    def remove_item(self, item):
        for i in range(len(self.item_inv)-1): 
            if self.item_inv[i] != None:
                if self.item_inv[i].id == item.id:
                    self.item_inv.remove(item)
                    self.item_inv.append(None)
                    break 
            else:
                continue

    def print_pet_inv(self): #prints the pet inventory
        Log("Pet Inventory")
        for pet in self.pet_inv:
            if pet != None:
                print(pet.name, end=" ")
        #Log(f"{self.pet_inv}")

    def print_item_inv(self): #prints the item inventory
        Log("Item Inventory")
        for item in self.item_inv:
            if item != None:
                print(item.name, end=" ")
        #Log(f"{self.item_inv}")