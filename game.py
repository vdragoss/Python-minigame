from rooms import LivingRoom, Kitchen, Study, Hallway, Yard
from player import Player


class Game(object):
    pass

rooms = {
        'Living room' : LivingRoom("Living room"),
        'Kitchen' : Kitchen("Kitchen"),
        'Hallway' : Hallway("Hallway"),
        'Study' : Study("Study"),
        'Yard' : Yard("Yard")
        }


# a.pick_up("map")
# a.view_map()


current_room = rooms['Living room']
print("You wake up confused and try to remember your name...")
a=Player()
print("")
if current_room.enter() == True:
    current_room.action(a)
next_room = ""

while True:
    print("")
    next_action = input("What's your next action?").lower()

    if any(substr in next_action for substr in ["move", "go", "enter", "change"]) :
        next_room = input("Where to?").capitalize()
        if next_room in current_room.exits:
            current_room = rooms[next_room]
            print("")
            if current_room.enter() == True:
                current_room.action(a)
        elif next_room == current_room.name :
            print("You are already here.")
        else:
            print("There's no door to that room.")

    elif any(substr in next_action for substr in ["look", "search", "investigate", "explore"]) :
        if current_room.look_around() == True:
            current_room.action(a)

    elif "knife" in next_action:
        if "Knife" in a.inventory:
            print("You don't want to cut yourself so you leave it in your jacket.")
        else:
            print("You don't have that.")

    elif "money" in next_action:
        if "Money" in a.inventory:
            print("It's still there, all $1000 of it.")
        else:
            print("You don't have that.")

    elif "inventory" in next_action :
        print("Inventory: ", a.inventory)
    elif "health" in next_action:
        print("You have ", a.health, "health")
    elif "map" in next_action:
        a.view_map()

    elif next_action in ["exit", "quit"] :
        print("Thank you for playing. Goodbye!")
        exit()

    else:
        print("I don't understand that")
