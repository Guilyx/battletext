# battle_game python project by ERWIN LEJEUNE#
##############################################
'''What's next ? : Use of the DEFENSE attribute
                   More fucking SPELLS

                   RANDOM events or triggered events like oh you're thrown thru
                   the fucking wall and took damage from this random event lolz

                   Upgrade to a more "Python" code

                   Add lolz messages like "Boom" "Waow" "Damn" "Stolended'st"

                   Specialization classes that inherit "CharacterClass"
                   Building a easy/medium/tough af ENEMY behavior
                   A defined SPECIALIZATION gets defined STATS
                    * If Warrior : no magic points
                    * If Paladin : a bit of both
                    * If Wizard : low attack, high magic, and more spells
                    (healing per exemple)
                   Add a "DODGING %"
                   MULTIPLAYER/ENEMY option (choose who you attack etc)
                   BALANCE the damage per classes
                   EXPAND to play within a local server
                   IMPLEMENT a secret JUGGERNAUT class that only I know about'''


from Classes.CharacterClass import*
from random import*
import time

#==============================================================================#

magic = [{"name": "Katon", "cost": 30, "damage": 150},
         {"name": "Raiton", "cost": 20, "damage": 105},
         {"name": "Fuuton", "cost": 5, "damage": 50},
         {"name": "Mokuton", "cost": 80, "damage": 205},
         {"name": "Suiton", "cost": 10, "damage": 65}]

#Character(HP, MP, ATTACK, DEFENSE, MAGICSPELL)

player = Character(800, 200, 100, 50, magic)
enemy = Character(1400, 80, 70, 20, magic)

enemy_currenthp = enemy.get_hp()
enemy_currentmp = enemy.get_mp()
player_currenthp = player.get_hp()
player_currentmp = player.get_mp()

#==============================================================================#

def printspaces():
    print("========================")

def turndelimitation():
    print(ColorsBook.OKGREEN + ColorsBook.BOLD +
         "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + ColorsBook.ENDC)
    print(ColorsBook.OKGREEN + ColorsBook.BOLD +
         "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + ColorsBook.ENDC)

def printdots():
    print("...")

def whoplays():
    joueur = randint(1, 2)
    return joueur

def randomevent(percentage):
    rdn = randint(0,100)
    if rdn <= (percentage):
        return True

def player_turn(enemy_currenthp, player_currentmp):
    action_choice = player.choose_action()
    printspaces()
    #IF ATTACK (CLOSE COMBAT)
    if action_choice == 0 :
        crit = randomevent(5)
        damage = player.generate_damage()
        if crit == True:
            print(ColorsBook.FAIL + ColorsBook.BOLD + "CRITICAL STRIKE" +
                  ColorsBook.ENDC)
            damage *= randint(2, 3)
        print("You have hit the enemy for " + ColorsBook.FAIL + str(damage) +
              ColorsBook.ENDC + " damage points !")
        printdots()
        enemy_currenthp = enemy.damage_taken(damage)
        print("The enemy has " + ColorsBook.OKGREEN + str(enemy_currenthp) +
              ColorsBook.ENDC + " HP left.")
        return(enemy_currenthp, player_currentmp)
        pass

    #IF MAGIC
    if action_choice == 1:
        spell_choice = player.choose_spell()
        printspaces()
        print("You chose : | ", player.get_spellname(spell_choice), " |")
        cost = player.get_spellcost(spell_choice)

        if (cost <= player_currentmp):
            player_currentmp = player.consumed_mp(cost)
            magic_damage = player.get_spelldamage(spell_choice)
            print("Your spell has hit the enemy by " + ColorsBook.FAIL +
                  str(magic_damage) + ColorsBook.ENDC + " damage points !!")
            enemy_currenthp = enemy.damage_taken(magic_damage)
            print("You have " + ColorsBook.OKBLUE + str(player_currentmp) +
                  ColorsBook.ENDC + " MP left.")
            print("The enemy has " + ColorsBook.OKGREEN + str(enemy_currenthp) +
                  ColorsBook.ENDC + " HP left.")
            return(enemy_currenthp, player_currentmp)
            pass
        else:
            print(ColorsBook.FAIL + ColorsBook.BOLD +
                 "You don't have enough MP !!!!" + "( " + ColorsBook.OKBLUE +
                 str(player_currentmp) + " )" + ColorsBook.ENDC)
            printdots()
            print("You wasted a round. The enemy has " + str(enemy_currenthp) +
                  " HP left.")
            return(enemy_currenthp, player_currentmp)
            pass

        pass

def enemy_turn(player_currenthp, enemy_currentmp):
    action_choice = randint(0,1)
    nomana = 0

    if action_choice == 0:
        crit = randomevent(5)
        damage = enemy.generate_damage()
        if crit == True:
            print(ColorsBook.FAIL + ColorsBook.BOLD +
                  "The enemy chose to FUCK YOU UP WITH HIS BEAR HANDS" +
                  ColorsBook.ENDC)
            damage *= randint(2,3)
        print("The enemy has hit you for " + ColorsBook.FAIL + str(damage) +
              ColorsBook.ENDC + " damage points !")
        printdots()
        player_currenthp = player.damage_taken(damage)
        print("You have " + ColorsBook.OKGREEN + ColorsBook.BOLD +
              str(player_currenthp) +  ColorsBook.ENDC + " HP left.")
        return(player_currenthp, enemy_currentmp)
        pass

    if action_choice == 1:
        spell_choice = randint(0, 4)
        print("The enemy casts | ", player.get_spellname(spell_choice), " |")
        time.sleep(2)
        cost = enemy.get_spellcost(spell_choice)

        if (cost <= enemy_currentmp):
            enemy_currentmp = enemy.consumed_mp(cost)
            magic_damage = enemy.get_spelldamage(spell_choice)
            print("His spell hits you hard...  " + ColorsBook.FAIL +
                  str(magic_damage) + ColorsBook.ENDC + " damage points !!")
            player_currenthp = player.damage_taken(magic_damage)
            print("You have " + ColorsBook.OKGREEN + ColorsBook.BOLD +
                  str(player_currenthp) + ColorsBook.ENDC + " HP left.")
            return(player_currenthp, enemy_currentmp)
            pass
        elif (cost > enemy_currentmp) and (nomana == 0):
            print(ColorsBook.FAIL + ColorsBook.BOLD + "The enemy tried to " +
                  "cast a spell... but he doesn't have enough MP !!" +
                  ColorsBook.ENDC)
            printdots()
            print("You still have " + ColorsBook.OKGREEN + ColorsBook.BOLD +
                  str(player_currenthp) + ColorsBook.ENDC + " HP left.")
            if enemy_currentmp == 0:
                nomana = 1
            return(player_currenthp, enemy_currentmp)
            pass

        pass


#==============================================================================#

player.printstats("AURAZUR")
turndelimitation()
enemy.printstats("ENEMY")

input("Press Enter to continue...")

time.sleep(5)

printspaces()
print(ColorsBook.FAIL + ColorsBook.BOLD + "AN ENEMY ATTACKS!" + ColorsBook.ENDC)

#==============================================================================#

who = whoplays()

while True:
    if who == 1:
        print(ColorsBook.BOLD + "It's your turn !" + ColorsBook.ENDC)
        enemy_currenthp, player_currentmp = player_turn(enemy_currenthp,
                                                        player_currentmp)
        turndelimitation()
        if enemy_currenthp == 0:
            break
        who = 2

    if who == 2:
        print("The enemy is about to make a move ... *roulement de tambourins*")
        printdots()
        time.sleep(5)
        print(ColorsBook.BOLD + "It's the enemy's turn !" + ColorsBook.ENDC)
        player_currenthp, enemy_currentmp = enemy_turn(player_currenthp,
                                                       enemy_currentmp)
        turndelimitation()
        if player_currenthp == 0:
            break
        time.sleep(5)
        who = 1

#==============================================================================#


if (enemy_currenthp == 0):
    print("Congratulations, you have won the " + ColorsBook.BOLD +
          ColorsBook.WARNING + "FIGHT !!" + ColorsBook.ENDC)

elif (player_currenthp == 0):
    print(ColorsBook.FAIL + ColorsBook.BOLD + "YOU ARE DEAD !" +
          ColorsBook.ENDC)

elif (enemy_currenthp == 0) and (player_currenthp == 0):
    print("It's a draw, wow rare bitch")
