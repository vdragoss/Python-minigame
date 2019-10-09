import json
from  actions import Action

with open("rooms.json") as f:
    d = json.load(f)

print(d['Living Room']['Name'])
print(d['Hallway']['Exits'])


class Room(object):

    def __init__ (self, name):
        self.name = name
        print("func, ", self, name)

    def enter(self):
        print("enter", Description)

class LivingRoom(object):

    def __init__ (self):
        Name = "Living Room"
        Description = f"Description {Name} bla bla"
        Contents = ["Map"]
        Exits = ["Hallway", "Kitchen"]
        print(Description)
        self.Action = Action()

    def attack(self):
        self.Action.attack()

    def pickUp(self):
        self.Action.pickUp()


class Kitchen(object):

    def __init__ (self):
        Name = "Kitchen"
        Description = f"Description {Name} bla bla"
        Contents = ["Knife"]
        Exits = ["Living Room","Hallway", "Study"]
        print(Description)
        self.Action = Action()

LivingRoom = Room("lr")
Kitchen = Room("kt")
print(LivingRoom.name)
print(Kitchen.name)
