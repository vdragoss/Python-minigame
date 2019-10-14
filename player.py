from random import randrange

class Player(object):

    stats = {}
    inventory = {}

    def __init__(self):
        pass

    def define_stats(self):
        print("Welcome")
        self.name = input("Name: ")
        print("Your health is determined by a 2d6 dye throw. You have 3 chances.")
        self.health = 2 * randrange(1,7)
        print("Your health is: ", self.health)
        for i in range(0,2):
            try_again = input("Try again? Yes/No: ")
            if try_again != "Yes":
                print("I'll take that as a 'No'. ")
                break
            elif try_again == "Yes" and i == 1:
                print("Final throw, let's hope for a good one")
            self.health = 2 * randrange(1,7)
            print("Your health is: ", self.health)




    def pickUp(self):
        print("pickUp")

    def attack(self):
        print("attack")

    def lockPick(self):
        print("lockPick")

    def viewMap(self):
        print("viewMap")

a=Player()
a.define_stats()
print("hlth", a.health)
