from random import randrange
from textwrap import dedent


class Player(object):


    def __init__(self):
        self.inventory = []
        self.name = input("Name: ")
        self.health = self.define_health()


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
            print("I don't understand that")


    def open_lock(self, safe):

        if safe.locked == True:
            safe.safe_is_locked()
            guess = input("You think for a while, then try: ")
            while guess != safe.combination:
                if input("Do you want to try again? ").lower() == "no":
                    print("You back away from the safe")
                    return False
                guess = input("Thinking harder, you try: ")
            print(f"The lock opens and you open the door, revealing the {safe.contents}")
            safe.locked = False
            return True
        else:
            print(f"The unlocked door swings freely, showing the {safe.contents} still inside")
            return True


    def investigate(self, room):
        if room.contents != "" and room.visited == False:
            print("Looking around, you notice a", room.contents, ".")
            room.visited = True
            return True
        elif room.contents != "" and room.visited == True:
            print("You notice the", room.contents, "is still there.")
            return True
        else:
            print("There is nothing of note here.")


    def use_item(self, item, room):
        if room.name != "Hallway":
            if item in self.inventory:
                print(f"You briefly take the {item} out, thinking of a possible use.")
            else:
                print("I don't understand that")
        else:
            if item in self.inventory:
                if item == "Knife":
                    print(dedent("""
                        The guard is taken by surprise by your action as your
                        plunge the knife deep into his heart."""))
                    return "Kill"
                elif item == "Money":
                    print(dedent("""
                        You take out the stack of cash and place it in the guard's
                        hand. He looks away, smirking."""))
                    return "Bribe"
            else:
                print("I don't understand that")
