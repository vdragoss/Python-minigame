import json
from random import randrange
from textwrap import dedent
from player import Player
from safe import Safe
from guard import Guard


with open("rooms.json") as f:
    d = json.load(f, strict=False)


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
            print(self.description, end='')
        else:
            print(self.description2)

    def action(self):
        """ Each room class has a specific action """


class LivingRoom(Room):

    def action(self, player):
        if input("Do you want to pick it up? \n>").lower() == "yes":
            player.add_item("Map")
            print("You pick it up and find the basic floor plan of a house.")
            self.contents = ""
            player.view_map()
            print("Carefully, you fold it in your pocket for future reference.")
        else:
            print("Ignoring it, you ponder your next move...")


class Kitchen(Room):

    def action(self, player):
        if input("Do you want to take it? \n>").lower() == "yes":
            player.add_item(self.contents)
            print("You put the", self.contents.lower(), "in your jacket.")
            self.contents = ""
        else:
            print("Ignoring it, you think about what to do next...")


class Study(Room):

    def action(self, player):
        if self.contents == "Locked safe":
            self.safe = Safe(str(player.health) + player.name,"Money")
        if input("Do you want to open it? \n>").lower() == "yes":
            if player.open_lock(self.safe) == True:
                if input(f"Do you take the {self.safe.contents}? \n>").lower() == "yes":
                    print(f"You quickly place the {self.safe.contents} into your back pocket")
                    player.add_item(self.safe.contents)
                    self.contents = ""
                else:
                    print("Better not steal.")
                    self.contents = "Unlocked safe"
        else:
            print("Ignoring it, you think about what to do next...")


class Hallway(Room):

    def __init__(self, name):
        super().__init__(name)
        self.guard=Guard()

    def action(self, player):
        if self.guard.alive == True:
            if self.guard.provoked == True:
                self.guard.punch(player)
                self.guard.provoked = False
            else:
                if input("Do you want to engage him? \n>").lower() == "yes":
                    self.guard.contact()
                else:
                    print("You try to avoid eye contact.")
        else:
            print("His body lies motionless, with a knife sticking out of his chest.")


class Yard(Room):

    def action(self,player):
        print("You have escaped the house. Congratulations!")
        exit()
