import random


class ColorsBook:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Character:
    def __init__(self, hp, mp, atk, dfs, magic):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk_low = atk - 10
        self.atk_high = atk + 10
        self.dfs = dfs
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    def get_spelldamage(self, index):
        magic_low = self.magic[index]["damage"] - 5
        magic_high = self.magic[index]["damage"] + 5
        return random.randrange(magic_low, magic_high)

    def damage_taken(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def consumed_mp(self, cost):
        self.mp -= cost

        if self.mp < 0:
            self.mp = 0

        return self.mp

    def get_spellname(self, index):
        return self.magic[index]["name"]

    def get_spellcost(self, index):
        return self.magic[index]["cost"]

    def choose_action(self):
        print("========================")
        index = 0
        print("Actions")
        for item in self.actions:
            print(str(index) + " : ", item)
            index += 1

        print("========================")

        choice = int(input("Choose your action | "))
        print("You chose : ", choice)
        return(choice)

    def choose_spell(self):
        print("========================")
        index = 0
        print("Magic Spells")
        for spell in self.magic:
            print(str(index) + " : ", spell["name"],
                  " (cost :", str(spell["cost"]) + " ) ")
            index += 1
        choice = input("Choose your spell | ")
        print("You chose : " + choice)
        return(int(choice))

    def printstats(self, name):
        index = 0
        print(name)
        print("========================")
        print("HP :", self.maxhp)
        print("MP :", self.maxmp)
        print("ATK MAX :", self.atk_high)
        print("DFS :", self.dfs)
        print("MAGIC SPELLS :")
        for spell in self.magic:
            print("Name : ", spell["name"], "|| Damage : ",
                  spell["damage"], " points")
        print("========================")
