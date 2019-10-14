from rooms import LivingRoom, Kitchen, Study, Hallway, Yard
from player import Player

class Game(object):
    pass

rooms = {
        'Living Room' : LivingRoom("Living Room"),
        'Kitchen' : Kitchen("Kitchen"),
        'Hallway' : Hallway("Hallway"),
        'Study' : Study("Study"),
        'Yard' : Yard("Yard")
        }

a=Player()
a.pick_up("horse")
print("inventory", a.inventory)
a.pick_up("map")
a.view_map()

current_room = rooms['Living Room']
print("You wake up in a strange living room.")
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
