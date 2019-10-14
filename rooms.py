import json

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
            self.visited = True
            if self.contents != []:
                print("Looking around, you notice a", *self.contents, ".")
            else:
                print("There is nothing of note here.")
        else:
            print("enter", self.description2)
            if self.contents != []:
                print("You notice the", *self.contents, "is still there.")
            else:
                print("There is nothing of note here.")




class LivingRoom(Room):
    pass

class Kitchen(Room):
    pass

class Study(Room):
    pass

class Hallway(Room):
    pass

class Yard(Room):
    pass
