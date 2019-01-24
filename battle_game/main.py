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
                   MULTIPLAYER/ENEMY option (choose who you attack etc)
                   BALANCE the damage per classes
                   EXPAND to play within a local server
                   IMPLEMENT a secret JUGGERNAUT class that only I know about'''


from Classes.CharacterClass import*

def printspaces():
    print("========================")

def printdots():
    print("...")

#==============================================================================#

magic = [{"name": "Katon", "cost": 30, "damage": 100},
         {"name": "Raiton", "cost": 10, "damage": 25},
         {"name": "Fuuton", "cost": 10, "damage": 25},
         {"name": "Mokuton", "cost": 10, "damage": 25},
         {"name": "Suiton", "cost": 10, "damage": 25}]

#Character(HP, MP, ATTACK, DEFENSE, MAGICSPELL)

player = Character(400, 65, 60, 34, magic)
enemy = Character(1200, 80, 40, 20, magic)

enemy_currenthp = enemy.get_hp()
enemy_currentmp = enemy.get_mp()
player_currenthp = player.get_hp()
player_currentmp = player.get_mp()


#==============================================================================#

printspaces()
print(ColorsBook.FAIL + ColorsBook.BOLD + "AN ENEMY ATTACKS!" + ColorsBook.ENDC)

#==============================================================================#

while not (enemy_currenthp == 0) or (player_currenthp == 0):

    action_choice = player.choose_action()

    #IF ATTACK (CLOSE COMBAT)
    if action_choice == 0 :
        damage = player.generate_damage()
        print("You have hit the enemy for " + str(damage) + " damage points !")
        printdots()
        enemy_currenthp = enemy.damage_taken(damage)
        print("The enemy has " + str(enemy_currenthp) + " HP left.")
        pass

    #IF MAGIC
    if action_choice == 1:
        spell_choice = player.choose_spell()
        print("You chose : | ", player.get_spellname(spell_choice), " |")
        cost = player.get_spellcost(spell_choice)

        if (cost <= player_currentmp):
            player_currentmp = player.consumed_mp(cost)
            magic_damage = player.get_spelldamage(spell_choice)
            enemy_currenthp = enemy.damage_taken(magic_damage)
            print("The enemy has " + str(enemy_currenthp) + " HP left.")
        else:
            print(ColorsBook.FAIL + ColorsBook.BOLD +
                 "You don't have enough MP !!!!" + ColorsBook.ENDC)
            printdots()
            print("The enemy has " + str(enemy_currenthp) + " HP left.")
            pass

        pass


#==============================================================================#


if (enemy_currenthp == 0):
    print("Congratulations, you have won the " + ColorsBook.BOLD +
          ColorsBook.WARNING + "FIGHT !!" + ColorsBook.ENDC)

elif (player_currenthp == 0):
    print(ColorsBook.FAIL + ColorsBook.BOLD + "YOU ARE DEAD !" +
          ColorsBook.ENDC)

elif (enemy_currenthp == 0) and (player_currenthp == 0):
    print("It's a draw, wow rare bitch")
