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
from Classes.Inventory import*
from random import*
import time

#==============================================================================#

#Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
superpotion = Item("Super-Potion", "potion", "Heals 100 HP", 100)
megapotion = Item("Mega-Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 99999)
ether = Item("Ether", "elixer", "Restores party's HP/MP", 999999)
sacredashes = Item("SacredAshes", "offense", "Deals 500 damage", 500)

playeritems = [{"item": potion, "quantity": 15},
               {"item": elixer, "quantity": 1},
               {"item": sacredashes, "quantity": 3}]
enemyitems = [{"item": potion, "quantity": 15},
              {"item": megapotion, "quantity": 8},
              {"item": sacredashes, "quantity": 5}]

#Character(HP, MP, ATTACK, DEFENSE, MAGICSPELL)
player1 = Character("AURAZUR:", 4700, 800, 750, 50, playeritems)
player2 = Character("BOB:    ", 400, 1000, 300, 45, playeritems)
enemy = Character(  "AKAGAMI:", 7500, 280, 515, 20, enemyitems)


enemy_currenthp = enemy.get_hp()
enemy_currentmp = enemy.get_mp()
player_currenthp = player1.get_hp()
player_currentmp = player1.get_mp()

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

def player_turn(player_currenthp, enemy_currenthp, player_currentmp,
                enemy_currentmp):

    action_choice = player1.choose_action()
    printspaces()
    #IF ATTACK (CLOSE COMBAT)
    if action_choice == 0 :
        crit = randomevent(5)
        damage = player1.generate_damage()
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
        return(player_currenthp, enemy_currenthp, player_currentmp,
               enemy_currentmp)
        pass

    #IF MAGIC
    elif action_choice == 1:
        spell_choice = player1.choose_spell()
        printspaces()
        print("You chose : | ", player1.get_spellname(spell_choice), " |")
        cost = player1.get_spellcost(spell_choice)

        if (cost <= player_currentmp):
            player_currentmp = player1.consumed_mp(cost)
            magic_damage = player1.get_spelldamage(spell_choice)

            if (player1.get_spelltype(spell_choice) == "Offense"):
                print("Your spell has hit the enemy by " + ColorsBook.FAIL +
                      str(magic_damage) + ColorsBook.ENDC + " damage points !!")
                enemy_currenthp = enemy.damage_taken(magic_damage)
                print("You have " + ColorsBook.OKBLUE + str(player_currentmp) +
                      ColorsBook.ENDC + " MP left.")
                print("The enemy has " + ColorsBook.OKGREEN + str(enemy_currenthp) +
                      ColorsBook.ENDC + " HP left.")
                return(player_currenthp, enemy_currenthp, player_currentmp,
                       enemy_currentmp)

            if (player1.get_spelltype(spell_choice) == "Support"):
                print("You have recovered " + ColorsBook.OKGREEN +
                      str(magic_damage) + ColorsBook.ENDC + " HP !")
                player_currenthp = player1.heal(magic_damage)
                print("You have " + ColorsBook.OKGREEN + str(player_currenthp) +
                      ColorsBook.ENDC + " HP left.")
                return(player_currenthp, enemy_currenthp, player_currentmp,
                       enemy_currentmp)
            pass

        else:
            print(ColorsBook.FAIL + ColorsBook.BOLD +
                 "You don't have enough MP !!!!" + "( " + ColorsBook.OKBLUE +
                 str(player_currentmp) + " )" + ColorsBook.ENDC)
            printdots()
            print("You wasted a round. The enemy has " + str(enemy_currenthp) +
                  " HP left.")
            return(player_currenthp, enemy_currenthp, player_currentmp,
                   enemy_currentmp)
            pass

        pass

    #IF ITEMS
    elif action_choice == 2:
        item_choice = player1.choose_item()
        item = player1.item[item_choice]["item"]

        if player1.item[item_choice]["quantity"] == 0:
            print(ColorsBook.FAIL + "NONE LEFT !!!" + ColorsBook.ENDC)
            return(player_currenthp, enemy_currenthp, player_currentmp,
                   enemy_currentmp)
            pass

        else:
            player1.item[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player_currenthp = player1.heal(item.prop)
                print(ColorsBook.WARNING + item.name + " heals you for ",
                      str(item.prop) + " HP (yay)." + ColorsBook.ENDC)
                pass

            elif item.type == "elixer":
                player_currenthp = player1.heal(item.prop)
                player_currentmp = player1.maxmp
                print(ColorsBook.WARNING + item.name +
                      " has fully restored your HP and MP" + ColorsBook.ENDC)
                pass

            elif item.type == "offense":
                enemy_currenthp = enemy.damage_taken(item.prop)
                print(ColorsBook.WARNING + item.name +
                      " has dealt " + str(item.prop) + " damage to the enemy." +
                      ColorsBook.ENDC)
                pass

        return(player_currenthp, enemy_currenthp, player_currentmp,
               enemy_currentmp)
        pass


def enemy_turn(player_currenthp, enemy_currenthp, player_currentmp,
               enemy_currentmp):
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
        player_currenthp = player1.damage_taken(damage)
        print("You have " + ColorsBook.OKGREEN + ColorsBook.BOLD +
              str(player_currenthp) +  ColorsBook.ENDC + " HP left.")
        return(player_currenthp, enemy_currenthp, player_currentmp,
               enemy_currentmp)
        pass

    if action_choice == 1:
        spell_choice = randint(0, 4)
        print("The enemy casts | ", player1.get_spellname(spell_choice), " |")
        time.sleep(2)
        cost = enemy.get_spellcost(spell_choice)

        if (cost <= enemy_currentmp):
            enemy_currentmp = enemy.consumed_mp(cost)
            magic_damage = enemy.get_spelldamage(spell_choice)

            if (enemy.get_spelltype(spell_choice) == "Offense"):
                print("His spell hits you hard...  " + ColorsBook.FAIL +
                      str(magic_damage) + ColorsBook.ENDC + " damage points !!")
                player_currenthp = player1.damage_taken(magic_damage)
                print("You have " + ColorsBook.OKGREEN + ColorsBook.BOLD +
                      str(player_currenthp) + ColorsBook.ENDC + " HP left.")
                return(player_currenthp, enemy_currenthp, player_currentmp,
                       enemy_currentmp)

            if (enemy.get_spelltype(spell_choice) == "Support"):
                print("The enemy has recovered " + ColorsBook.OKGREEN +
                      str(magic_damage) + ColorsBook.ENDC + " HP !")
                enemy_currenthp = enemy.heal(magic_damage)
                print("He now has " + ColorsBook.OKGREEN + str(enemy_currenthp) +
                      ColorsBook.ENDC + " HP left.")
                return(player_currenthp, enemy_currenthp, player_currentmp,
                       enemy_currentmp)

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
            return(player_currenthp, enemy_currenthp, player_currentmp,
                   enemy_currentmp)
            pass

        pass


#==============================================================================#
printspaces()
print(ColorsBook.FAIL + ColorsBook.BOLD + "AN ENEMY ATTACKS!" + ColorsBook.ENDC)

input("Press Enter to continue...")
player1.printstats()
printspaces()
enemy.printstats()
time.sleep(3)
#==============================================================================#

who = whoplays()

while True:
    if who == 1:
        print(ColorsBook.BOLD + "It's your turn !" + ColorsBook.ENDC)
        player_currenthp, enemy_currenthp, player_currentmp, enemy_currentmp = player_turn(player_currenthp,
                                                                                           enemy_currenthp,
                                                                                           player_currentmp,
                                                                                           enemy_currentmp)
        turndelimitation()
        player1.printstats()
        printspaces()
        enemy.printstats()
        if enemy_currenthp == 0:
            break
        who = 2

    if who == 2:
        print("The enemy is about to make a move ... *roulement de tambourins*")
        printdots()
        time.sleep(3)
        print(ColorsBook.BOLD + "It's the enemy's turn !" + ColorsBook.ENDC)
        player_currenthp, enemy_currenthp, player_currentmp, enemy_currentmp = enemy_turn(player_currenthp,
                                                                                           enemy_currenthp,
                                                                                           player_currentmp,
                                                                                           enemy_currentmp)
        turndelimitation()
        player1.printstats()
        printspaces()
        enemy.printstats()
        if player_currenthp == 0:
            break

        time.sleep(3)
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
