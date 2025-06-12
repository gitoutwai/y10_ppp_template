from tank import Tank
from random import choice
from random import randint

# Player settings
tanks = {}
Germany = "Germany"
France = "France"
Britain = "Britain"
USA = "USA"
USSR = "USSR"
nations = [Germany, France, Britain, USA, USSR]
hitTypes = ["direct hit", "ricochet", "miss", "non-penetrate"]

playerNation = ""
while playerNation not in nations:
    playerNation = input("Choose your nation: ")

nations.remove(playerNation)

# Tank initiation
tanks["Panzer IV F2"] = Tank("Panzer IV F2", Germany, 300)
tanks["Somua S35"] = Tank("Somua S35", France, 300)
tanks["Crusader III"] = Tank("Crusader III", Britain, 200)
tanks["M4A2(75)"] = Tank("M4A2(75)", USA, 500)
tanks["T-34/85"] = Tank("T-34/85", USSR, 500)

tankEnemies = []
for t in tanks.keys():
    if playerNation == tanks[t].nation:
        playerTank = t
        print(f"Your tank is the {playerTank}")
    else:
        tankEnemies.append(t)

# tankUsed = input("What is the tank you wish to use: ") - add later for more tanks per nation

# Enemy selection
enemy = choice(tankEnemies)
print(f"Your enemy is {enemy} from {tanks[enemy].nation}!")
battle = input("Do you wish to start the battle?(y/n)").lower()
while battle == "y":
    shell = input("What is the shell used: ")
    while shell not in tanks[playerTank].shellTypes:
        shell = input("What is the shell used: ")

    # Striking the enemy
    tanks[playerTank].attack(shell, enemy)
    hit = choice(hitTypes)
    print(f"You scored a {hit}!")
    if hit == "direct hit":
        tanks[enemy].damaged(randint(200, 400))
    elif hit == "ricochet":
        tanks[enemy].damaged(randint(0, 50))
    elif hit == "miss":
        pass
    elif hit == "non-penetrate":
        tanks[enemy].damaged(randint(0, 100))

    tanks[enemy].checkstats()
    
    if tanks[enemy].hp > 0:
        # Enemy striking the player
        tanks[enemy].attack(shell, playerTank)
        hit = choice(hitTypes)
        print(f"The enemy scored a {hit}!")
        if hit == "direct hit":
            tanks[playerTank].damaged(randint(200, 400))
        elif hit == "ricochet":
            tanks[playerTank].damaged(randint(0, 50))
        elif hit == "miss":
            pass
        elif hit == "non-penetrate":
            tanks[playerTank].damaged(randint(0, 100))

        tanks[playerTank].checkstats()
    else:
        print(f"{enemy} has been defeated!")
        battle = "n"