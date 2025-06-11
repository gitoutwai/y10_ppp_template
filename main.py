from tank import Tank

# Initiation
tanks = {}
Germany = "Germany"
France = "France"
Britain = "Britain"
USA = "USA"
USSR = "USSR"

nations = [Germany, France, Britain, USA, USSR]
playerNation = input("Choose your nation: ")
nations.remove(playerNation)

# Tank initiation
tanks["Panzer IV F2"] = Tank("Panzer IV F2", Germany, 500)
tanks["Somua S35"] = Tank("Somua S35", France, 300)

tankUsed = input("What is the tank you wish to use: ")

shell = input("What is the shell used: ")
if shell in tanks[tankUsed].shellTypes:
    print("you have ths shell")
else:
    print("you don't have this shell") 
enemy = input("Who is the enemy: ")
tanks["Panzer IV F2"].attack(shell, enemy)
tanks[enemy].damaged(200)
tanks[enemy].checkstats()