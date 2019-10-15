from random import randrange
from textwrap import dedent


class Player(object):


    def __init__(self):
        self.inventory = []
        self.name = input("Name: ")
        self.health = self.define_health()
        self.locked = True
        self.guarded = True
        pass

    def define_health(self):
        print(dedent("""
            You feel weak and injured. Let's see your health.
            ***Your health is determined by a 3d6 dye throw. You have 3 chances.***
            """))
        input(">")
        health = 3 * randrange(1,7)
        print("Your health is: ", health, "/100")
        for i in range(0,2):
            try_again = input("Try again? Yes/No: ").lower()
            if try_again == "no":
                break
            elif try_again != "yes":
                print("I'll take that as a 'No'. ")
                break
            elif try_again == "yes" and i == 1:
                print("Final throw, let's hope for a good one")
            health = 2 * randrange(1,7)
            print("Your new health is: ", health, "/100")
        print("Your final health is: ", health, "/100")
        return health


    def add_item(self, item):
        self.inventory.append(item)


    def view_map(self):
        if "Map" in self.inventory:
            map = open("map.map", 'r')
            print(map.read())
        else:
            print("You don't have the map.")


    def pick_lock(self):
        combination = str(self.health) + self.name
        if self.locked == True:
            print(dedent("""
                It seems the safe is locked with a strange combination. It reads:
                Health comes first, \nAnd then your name
                Solve this puzzle \nFame, fame, fame.
                """))
            guess = input("You think for a while, then try: ")
            while guess != combination:
                if input("Do you want to try again? ").lower() == "no":
                    print("You back away from the safe")
                    return False
                guess = input("You think for a while, then try: ")
            print("The lock opens and you open the door, revealing a stack of cash")
            self.locked = False
            return True
        else:
            print("The unlocked door swings freely, showing the money still inside")
            return True


    def use(self, item):
        print("use", item)
