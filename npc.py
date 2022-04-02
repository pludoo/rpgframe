class NPC:
    def __init__(self, name, inv):
        self.name = name
        self.inv = inv

    def talk(self, dialog):
        print(f"{self.name}: {dialog}")
        