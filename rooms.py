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
            print("enter", self.description)
            self.visited = True
        else:
            print("enter", self.description2)

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
# LivingRoom.enter()
# LivingRoom.enter()
# Kitchen.enter()
# Kitchen.enter()
# LivingRoom.enter()

current_room = rooms['Living Room']
next_room = ""
print(current_room.name)
while True:
    if current_room != next_room:
        current_room.enter()
    next_room = input("Where do you want to go next?")
    if next_room in current_room.exits:
        current_room = rooms[next_room]
    else:
        print("Try again")
