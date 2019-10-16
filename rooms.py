import json
from player import Player
from random import randrange
from textwrap import dedent
from safe import Safe


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
        else:
            print("enter", self.description2)


    def action(self):
        """ Each room class has a specific action """


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
        if self.contents == "Locked safe":
            self.safe = Safe(str(player.health) + player.name,"Money")
        if input("Do you want to open it? ").lower() == "yes":
            if player.open_lock(self.safe) == True:
                if input(f"Do you take the {self.safe.contents}?").lower() == "yes":
                    print(f"You quickly place the {self.safe.contents} into your back pocket")
                    player.add_item(self.safe.contents)
                    self.contents = ""
                else:
                    print("Better not steal.")
                    self.contents = "Unlocked safe"
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
