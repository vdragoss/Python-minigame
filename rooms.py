import json
from  actions import Action

with open("rooms.json") as f:
    d = json.load(f)


class Room(object):

    def __init__ (self, name, description, contents, exits):
        self.name = name
        self.description = description
        self.contents = contents
        self.exits = exits
        self.Action = Action()

    def enter(self):
        print("enter", Description)

    def attack(self):
        self.Action.attack()

    def pickUp(self):
        self.Action.pickUp()


LivingRoom = Room(d['1']['Name'],d['1']['Description'],d['1']['Contents'],d['1']['Exits'])
print(LivingRoom.name, LivingRoom.exits)
