import json
from  actions import Action

with open("rooms.json") as f:
    d = json.load(f)


class Room(object):

    def __init__ (self, name):
        self.name = d[f'{name}']['Name']
        self.description = d[f'{name}']['Description']
        self.description2 = d[f'{name}']['Description2']
        self.contents = d[f'{name}']['Contents']
        self.exits = d[f'{name}']['Exits']
        self.visited = False

    def enter(self):

        if self.visited == False:
            print(self.description)
            self.visited = True
            if self.contents != []:
                print("Looking around, you notice a", *self.contents, ".")
            else:
                print("There is nothing of note here.")
        else:
            print("enter", self.description2)
            if self.contents != []:
                print("You notice the", *self.contents, "is still there.")
            else:
                print("There is nothing of note here.")




class LivingRoom(Room):
    pass

class Kitchen(Room):
    pass

class Study(Room):
    pass

class Hallway(Room):
    pass

class Yard(Room):
    pass


rooms = {
        'Living Room' : LivingRoom("Living Room"),
        'Kitchen' : Kitchen("Kitchen"),
        'Hallway' : Hallway("Hallway"),
        'Study' : Study("Study"),
        'Yard' : Yard("Yard")
        }


current_room = rooms['Living Room']
print("You wake up in a strang living room.")
current_room.enter()
next_room = ""

while True:
    next_room = input("Where do you want to go next?")
    if next_room in current_room.exits:
        current_room = rooms[next_room]
        current_room.enter()
    elif next_room == current_room.name :
        print("You are already here.")
    else:
        print("There's no door to that room.")
