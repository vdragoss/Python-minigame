from rooms import LivingRoom, Kitchen, Study, Hallway, Yard
from player import Player
from guard import Guard
from textwrap import dedent

class Game(object):

    def __init__(self,start_room):
        self.rooms = {
                'Living room' : LivingRoom("Living room"),
                'Kitchen' : Kitchen("Kitchen"),
                'Hallway' : Hallway("Hallway"),
                'Study' : Study("Study"),
                'Yard' : Yard("Yard")
                }
        self.start_room = self.rooms[start_room]


    def play(self, player):
        current_room = self.start_room
        next_room = ""
        current_room.enter()
        if a.investigate(current_room) == True:
            current_room.action(a)
        while True:
            next_action = input("\nWhat's your next action? >").lower()

            if any(substr in next_action for substr in ["move", "go", "enter", "change", "leave", "room"]) :
                next_room = input("Where to? >").capitalize()
                if next_room in current_room.exits:
                    if next_room == "Yard":
                        if current_room.guard.alive == True and current_room.guard.friend == False:
                            current_room.guard.provoked = True
                            current_room.action(a)
                        elif current_room.guard.alive == False:
                            print("You walk past the dead guard and through the door.")
                            current_room = self.rooms[next_room]
                            current_room.action(a)
                        elif current_room.guard.friend == True:
                            print("You walk through the door as the guard sits idly.")
                            current_room = self.rooms[next_room]
                            current_room.action(a)
                    else:
                        current_room = self.rooms[next_room]
                        current_room.enter()

                    if current_room.visited == False: #decide if player automatically investigates on first visit to room
                        if a.investigate(current_room) == True:
                            current_room.action(a)
                elif next_room == current_room.name :
                    print("You are already here.")
                else:
                    print("There's no door to that room.")

            elif any(substr in next_action for substr in ["look", "search", "investigate", "explore", "interact"]) :
                if a.investigate(current_room) == True:
                    current_room.action(a)

            elif "knife" in next_action:
                if a.use_item("Knife", current_room) == "Kill":
                    current_room.guard.alive = False
                    current_room.contents = "dead guard"

            elif "money" in next_action:
                if a.use_item("Money", current_room) == "Bribe":
                    current_room.guard.friend = True

            elif "map" in next_action:
                a.view_map()

            elif "room" in next_action:
                print("You are in the", current_room.name)
            elif "inventory" in next_action :
                print("Inventory: ", a.inventory)
            elif "health" in next_action:
                print("You have ", a.health, "health")


            elif next_action in ["exit", "quit"] :
                print("Thank you for playing. Goodbye!")
                exit()

            else:
                print("I don't understand that")



print(dedent("""
    Welcome. This is a minigame written in python and was developed as an exercise.
    The project can be found on Github: https://github.com/vdragoss/lpthw-minigame.
    The scope of the game is to escape a house you find yourself trapped in. You can
    *move* through the rooms, *search* them and *use* whatever items you find.
    Let's begin!

    """))
print("You wake up confused and try to remember your name...")
a=Player()
game = Game("Living room")
game.play(a)
