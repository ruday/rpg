import random
from .magic import Spell


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.name = name
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_actions(self):
        i = 1
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "ACTIONS" + bcolors.ENDC + "\n")
        for item in self.actions:
            print("     " + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("     " + str(i) + ":", spell.name, spell.cost, str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("     " + str(i) + ":", item["item"].name, ":", item["item"].description,
                  " (x" + str(item["quantity"]) + ")")
            i += 1

    def get_stats(self):
        hp_bar = ""
        mp_bar = ""
        hp_bar_ticks = (self.hp / self.maxhp) * 100 / 4
        mp_bar_ticks = (self.mp / self.maxmp) * 100 / 10

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_hp = ""
        current_mp = ""
#hp string
        if len(hp_string) < 9:
            hp_decreased = 9 - len(hp_string)

            while hp_decreased > 0:
                current_hp += " "
                hp_decreased -= 1

            current_hp += hp_string
        else:
            current_hp = hp_string

#mp string
        if len(mp_string) < 9:
            mp_decreased = 9 - len(mp_string)

            while mp_decreased > 0:
                current_mp += " "
                mp_decreased -=1

            current_mp += mp_string
        else:
          current_mp = mp_string



        print("                      _______________________________________                ________________ ")
        print(bcolors.BOLD + self.name + "    " + bcolors.ENDC + bcolors.BOLD +
              current_hp + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC + bcolors.BOLD + "|" + bcolors.ENDC + bcolors.BOLD + "    " +
              current_mp + " |" + bcolors.OKBLUE +
              mp_bar + bcolors.ENDC + bcolors.BOLD +
              "|" + bcolors.ENDC)


"""
player_items = [{"item": potion, "quantity": 5}, {"item": highpotion, "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixir, "quantity": 5},
                {"item": hielixir, "quantity": 5}, {"item": grenade, "quantity": 5}]
"""
