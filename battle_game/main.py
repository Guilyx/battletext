# battle_game python project

import CharacterClass

magic = [{"name": "Katon", "cost": 10, "damage": 25},
         {"name": "Raiton", "cost": 10, "damage": 25},
         {"name": "Fuuton", "cost": 10, "damage": 25},
         {"name": "Mokuton", "cost": 10, "damage": 25},
         {"name": "Suiton", "cost": 10, "damage": 25}]

player = Character(400, 65, 60, 34, magic)
enemy = Character(1200, 80, 40, 20, magic)

print(bcolor.FAIL + bcolor.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
while True:
    print("========================")
    player.choose_action()

    running = False
