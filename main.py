from tank import Tank
from battle import Battle
from shells import Shell

# Player settings
tanks = {}
Germany = "Germany"
France = "France"
Britain = "Britain"
USA = "USA"
USSR = "USSR"
nations = [Germany, France, Britain, USA, USSR]
hitTypes = ["direct hit", "ricochet", "miss", "non-penetrate"]
locations = {"Western Europe":0,
             "Eastern Europe":0,
             "Southern Europe":0,
             "Northern Europe":0,
             "temp":10}

currentLoc = "Western Europe"

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
game = True
while game:
    while (currentLoc == "temp" and len(locations) > 1) or (locations[currentLoc] >= 10 and len(locations) > 1):
        
        if currentLoc != "temp":
            del locations[currentLoc]
        
        if len(locations) == 1:
            break

        inputLoc = input("You have completed this level, where would you like to go next? ")
        if inputLoc in locations:
            currentLoc = inputLoc
        else:
            print("Location does not exist!")
            currentLoc = "temp"
    
    if len(locations) == 1:
        print("Well done! You have won the game!")
        game = False
        break
            
    
    action = input("What do you want to do? ")
    if action == "battle":
        Battle.battle(playerTank, tankEnemies, tanks, hitTypes, locations, currentLoc)
    elif action == "relocate":
        inputLoc = input("Where do you want to relocate to? ")
        if inputLoc in locations:
            if locations[inputLoc] < 10:
                currentLoc = inputLoc
                tanks[playerTank].relocate(inputLoc)
            else:
                print("That level has been completed already!")
                del locations[inputLoc]
            

        elif inputLoc == "repair shop":
            repair = input("Would you like to repair your tank?(y/n) ")
            if repair == "y" and tanks[playerTank].money >= 10:
                tanks[playerTank].money -= 10
                print("Your tank has been repaired!")
                tanks[playerTank].hp = tanks[playerTank].maxhp
        else:
            print("That location does not exist!")
    if action == "check stats":
        print(f"\nYou have {tanks[playerTank].money}$ and your tank has {tanks[playerTank].hp} health points!\nYou have completed {locations[currentLoc]} successful battles in {currentLoc}!\n")