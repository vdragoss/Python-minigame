from random import randrange
from textwrap import dedent

class Guard(object):

    def __init__(self):
        self.health = 2 * randrange(1,7)
        self.provoked = False
        self.alive = True
        self.friend = False
        self.surprised = True

    def punch(self, player):
        self.surprised = False
        damage = randrange(1,7)
        print(dedent(f"""
            You try and pass the guard but he punches you dealing {damage} damage."""))
        player.health -= damage
        if player.health <= 0:
            print(dedent("""
                You fall, and your life flashes before your eyes...
                You are now dead """))
            exit()
        else:
            print(dedent(f""" You take the punch and your health drops to {player.health}.
                As the guard watches your every move, you carefully consider
                what to do next. """))
