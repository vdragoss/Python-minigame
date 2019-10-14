from random import randrange

class Player(object):


    def __init__(self):
        self.inventory = []
        self.name = input("Welcome! What is your name? \nName: ")
        self.health = self.define_health()
        pass

    def define_health(self):
        print("Your health is determined by a 2d6 dye throw. You have 3 chances.")
        health = 2 * randrange(1,7)
        print("Your health is: ", health)
        for i in range(0,2):
            try_again = input("Try again? Yes/No: ")
            if try_again != "Yes":
                print("I'll take that as a 'No'. ")
                break
            elif try_again == "Yes" and i == 1:
                print("Final throw, let's hope for a good one")
            health = 2 * randrange(1,7)
            print("Your health is: ", health)
        return health




    def pick_up(self, item):
        print("pickUp")
        self.inventory.append(item)

    def view_map(self):
        print("""viewMap""")
        if "map" in self.inventory:
            map = open("map.map", 'r')
            print(map.read())
        else:
            print("You have no recollection of this place.")


    def attack(self):
        print("attack")

    def pick_lock(self):
        print("lockPick")
