def text_to_id(string): #this function adds up ascii values of each character to get a completely unique id
    total = 0
    for char in string:
        total += ord(char)
    return str(total) + string.upper()


class Item:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.id = text_to_id(self.name)