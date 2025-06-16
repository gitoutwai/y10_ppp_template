from random import choice
from random import randint

class Battle:
    def battle(playerTank, tankEnemies, tanks, hitTypes, location, currentLoc):
        # Enemy selection
        enemy = choice(tankEnemies)
        print(f"Your enemy is {enemy} from {tanks[enemy].nation}!")
        battle = input("Do you wish to start the battle?(y/n) ").lower()
        if battle == "n":
            print("You are attempting to maneuver away...")
            success = choice(["yes", "no"])
            if success == "yes":
                print("You have escaped!")
            else:
                print("You have been discovered!")
                battle = "y"

        while battle == "y":
            if tanks[playerTank].hp > 0:
                shell = input("What is the shell used: ")
                while shell not in tanks[playerTank].shellTypes:
                    shell = input("What is the shell used: ")
            else:
                print("You have been defeated! Head to the repair shops!")
                battle = "n"
                tanks[enemy].hp = tanks[enemy].maxhp
                break

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
                tanks[playerTank].money += 20
                location[currentLoc] += 1
                battle = "n"
                tanks[enemy].hp = tanks[enemy].maxhp
                break