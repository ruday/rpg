import random

class Spell:
        def __init__(self, name, cost, dmg, type):
            self.name = name
            self.cost = cost
            self.dmg = dmg
            self.type = type
            self.dmgh = dmg + 15
            self.dmgl = dmg - 15

        def generate_damage(self):
            low = self.dmg - 15
            high = self.dmg + 15
            return random.randrange(low, high)

"""
#create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

#create white magic
cure = Spell("Cure", 10, 100, "white")
cura = Spell("Cura", 18, 200, "white")
"""
