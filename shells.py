from random import randint
from random import choice

class Shell:
    def __init__(self, type, calibre):
        self.type = type
        self.calibre = calibre

    def damage(self):
        if self.type == "APCBC":
            hittypes = choice(["direct hit", "direct hit", "ricochet", "miss", "non-penetrate"])
            if hittypes == "direct hit":
                damage = (randint(200, 400) * (self.calibre/10))
            elif hittypes == "ricochet":
                damage = (randint(0, 50) * (self.calibre/10))
            elif hittypes == "miss":
                damage = 0
            elif hittypes == "non-penetrate":
                damage = (randint(0, 100) * (self.calibre/10))
        elif self.type == "HE":
            hittypes = choice(["direct hit", "ricochet", "miss", "non-penetrate", "non-penetrate", "non-penetrate"])
            if hittypes == "direct hit":
                damage = (randint(0, 100) * (self.calibre/10))
            elif hittypes == "ricochet":
                damage = (randint(0, 5) * (self.calibre/10))
            elif hittypes == "miss":
                damage = 0
            elif hittypes == "non-penetrate":
                damage = (randint(0, 10) * (self.calibre/10))
        elif self.type == "APHE":
            hittypes = choice(["direct hit", "ricochet", "miss", "non-penetrate"])
            if hittypes == "direct hit":
                damage = (randint(300, 500) * (self.calibre/10))
            elif hittypes == "ricochet":
                damage = (randint(0, 100) * (self.calibre/10))
            elif hittypes == "miss":
                damage = 0
            elif hittypes == "non-penetrate":
                damage = (randint(0, 200) * (self.calibre/10))

        return damage