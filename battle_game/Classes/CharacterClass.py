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
    def __init__(self, name, hp, mp, atk, dfs, item):
        self.name = name
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atk_low = atk - 10
        self.atk_high = atk + 10
        self.dfs = dfs
        self.item = item
        self.aesthetics = "    "
        self.magic = [{"name": "Fire", "cost": 120, "damage": 370, "type": "Offense"},
                 {"name": "Thunder", "cost": 100, "damage": 255, "type": "Offense"},
                 {"name": "Hurricane", "cost": 35, "damage": 150, "type": "Offense"},
                 {"name": "Quake", "cost": 180, "damage": 405, "type": "Offense"},
                 {"name": "Blizzard", "cost": 80, "damage": 125, "type": "Offense"},
                 {"name": "First Heal", "cost": 150, "damage": 260, "type": "Support"},
                 {"name": "Partial Heal", "cost": 300, "damage": 400, "type": "Support"}]
        self.actions = ["Attack", "Magic", "Items"]


    def getmagic(self):
        return self.magic

    def generate_damage(self):
        return random.randrange(self.atk_low, self.atk_high)

    def get_spelldamage(self, index):
        magic_low = int(self.magic[index]["damage"] - 0.1 * self.magic[index]["damage"])
        magic_high = int(self.magic[index]["damage"] + 0.1 * self.magic[index]["damage"])
        return random.randrange(magic_low, magic_high)

    def get_spelltype(self, index):
        spelltype = self.magic[index]["type"]
        return spelltype

    def heal(self, damage):
        self.hp += damage
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

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
            print(self.aesthetics, str(index) + " : ", item)
            index += 1

        print("========================")

        choice = int(input("Choose your action | "))
        print("You chose : ", choice)
        return(choice)

    def choose_spell(self):
        print("========================")
        index = 0
        print(ColorsBook.OKBLUE + ColorsBook.BOLD +
              "SPELLS" + ColorsBook.ENDC)
        for spell in self.magic:
            print(self.aesthetics, str(index) + " : ", spell["name"],
                  " ( cost :", str(spell["cost"]), ")",
                  "type : ", str(spell["type"]) + " ) ")
            index += 1
        print("========================")
        choice = input("Choose your spell | ")
        return(int(choice))

    def choose_item(self):
        print("========================")
        index = 0
        print(ColorsBook.WARNING + ColorsBook.BOLD +
              "ITEMS" + ColorsBook.ENDC)
        for item in self.item:
            print(self.aesthetics, str(index) + " : ", item["item"].name, " : ",
                  item["item"].description, " (*", item["quantity"], ")")
            index += 1
        print("========================")
        choice = input("Choose your item | ")
        return(int(choice))


    def printstats(self):
        hp_bar = ''
        mana_bar = ''
        bar_ticks = (self.hp / self.maxhp) * 25
        mana_bar_ticks = (self.mp / self.maxmp) * 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mana_bar_ticks > 0:
            mana_bar += "█"
            mana_bar_ticks -= 1

        while len(mana_bar) < 10:
            mana_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        mp_string = str(self.mp) + "/" + str(self.maxmp)

        current_mp = ""
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string

        else:
            current_hp = hp_string

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1
            current_mp += mp_string

        else:
            current_mp = mp_string

        print("NAME                 HP                                    MP")
        print("                      _________________________             __________")
        print(ColorsBook.BOLD + self.name + "   " +
              current_hp + " |" + ColorsBook.OKGREEN + hp_bar +
              ColorsBook.ENDC + ColorsBook.BOLD + "|   " +
              mp_string + " |" + ColorsBook.OKBLUE + mana_bar + ColorsBook.ENDC + "|")
        print("\n\n")
