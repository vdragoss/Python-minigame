from textwrap import dedent


class Safe(object):

    def __init__(self, combination, contents):
        self.combination = combination
        self.locked = True
        self.contents = contents

    def safe_is_locked(self):
        print(dedent("""
            It seems the safe is locked with a strange combination. It reads:
            Health comes first,
            And then your name.
            Solve this puzzle,
            Fame, fame, fame.
            """))

    def safe_is_unlocked(self):
        print(f"The unlocked door swings freely, showing the {self.contents} still inside")
