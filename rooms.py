import json
from player import Player
from random import randrange
from textwrap import dedent


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
            return self.look_around()
        else:
            print("enter", self.description2)
            return self.look_around()


    def look_around(self):
        if self.contents != "" and self.visited == False:
            print("Looking around, you notice a", self.contents, ".")
            self.visited = True
            return True
        elif self.contents != "" and self.visited == True:
            print("You notice the", self.contents, "is still there.")
            return True
        else:
            print("There is nothing of note here.")

    def action(self):
        """ Each room class has a specific action"""


class LivingRoom(Room):

    def action(self, player):
        if input("Do you want to pick it up? ").lower() == "yes":
            player.add_item(self.contents)
            print("You pick it up and find the basic floor plan of a house.")
            self.contents = ""
            player.view_map()
            print("Carefully, you fold it in your pocket for future reference.")
        else:
            print("Ignoring it, you ponder your next move...")


class Kitchen(Room):

    def action(self, player):
        if input("Do you want to take it? ").lower() == "yes":
            player.add_item(self.contents)
            print("You put the", self.contents.lower(), "in your jacket.")
            self.contents = ""
        else:
            print("Ignoring it, you think about what to do next...")


class Study(Room):

    def action(self, player):
        if input("Do you want to open it? ").lower() == "yes":
            if player.pick_lock() == True:
                if input("Do you take the money?").lower() == "yes":
                    print("You quickly place the money into your back pocket")
                    player.add_item("Money")
                    self.contents = ""
                else:
                    print("Better not steal.")
        else:
            print("Ignoring it, you think about what to do next...")

class Hallway(Room):

    def action(self, player):
        if input("Do you want to engage him? ").lower() == "yes":
            print("He effortlessly pushes you aside.")
        else:
            print("You try to avoid eye contact.")

class Yard(Room):
    def action(self, player):
        if player.guarded == True:
            punch = randrange(1,7)
            print(f"You try and pass the guard but he punches you dealing {punch} damage.")
            player.health -= punch
            if player.health <= 0:
                print("You fall, and your life flashes before your eyes.. \nYou are dead")
                exit()
            else:
                print(dedent(f"""
                    You take the punch and with {player.health} health left you
                    carefully consider your next move.
                    """))
        else:
            print("Congratulations! You escaped the house")
            exit()
