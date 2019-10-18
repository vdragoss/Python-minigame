from random import randrange
from textwrap import dedent


class Guard(object):

    def __init__(self):
        self.health = 2 * randrange(1,7)
        self.provoked = False
        self.alive = True
        self.friend = False
        self.startled = False

    def punch(self, player):
        self.startled = True
        damage = randrange(1,7)
        print(dedent(f"""
            You try and pass the guard but he punches you dealing {damage} damage."""), end='')
        player.health -= damage
        if player.health <= 0:
            print(dedent("""
                You fall, and your life flashes before your eyes...
                You are now dead """))
            input("Press any key to exit: >")
            exit()
        else:
            print(dedent(f"""
                You take the punch and your health drops to {player.health}.
                As the guard watches your every move, you carefully consider
                what to do next. """))

    def contact(self):
        if self.friend == True:
            print(dedent("""
                The guard nods and greets you, stepping out of the way."""))
        elif self.friend == False and self.startled == False:
            print(dedent("""
                You approach while he calmly ignores you. As you reach him,
                he grunts and effortlessly pushes you aside. If only you
                could somehow get past, or make him leave..."""))
        elif self.friend == False and self.startled == True:
            print(dedent("""
                You try to approach again but every step is met with a menacing
                stare. You stop in your tracks and consider your next move..."""))
