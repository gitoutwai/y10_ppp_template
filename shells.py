from random import randint

class Shell:
    def __init__(self, name, type, calibre):
        self.name = name
        self.type = type
        self.calibre = calibre

        def damage(self):
            if self.type == "APCBC":
                damage = randint(200, 500)