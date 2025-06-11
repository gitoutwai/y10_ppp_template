class Pokemon:
    def __init__(self, name, type, hp):
        self.name = name
        self.type = type
        self.hp = hp
    
    def attack(self, move):
        print(f"{self.name} used {move}!")

charz = Pokemon("Charizard", "fire", "300")
charz.attack("burn")