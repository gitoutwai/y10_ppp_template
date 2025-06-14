from shells import Shell

class Tank:
    def __init__(self, name, nation, hp):
        self.name = name
        self.nation = nation
        self.hp = hp
        self.maxhp = hp
        self.shellTypes = ["APCBC", "HE", "APHE"]
        self.money = 100

    def checkstats(self):
        print(f"The {self.name} has {self.hp} hp!")

    def damaged(self, value):
        print(f"The {self.name} has been dealt {value} hp of damage!")
        self.hp -= value

    def attack(self, shell, victim):
        print(f"{self.name} fired {shell} on {victim}!")
    
    def relocate(self, location):
        print(f"{self.name} has relocated to {location}!")
    
    def training(self, skill, time):
        print(f"{self.name} is training {skill} skills for {time} hours!")