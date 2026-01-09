import random

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def use_weapon(self):
        print(f"Swung the {self.name}")
        min_dmg = self.damage - 5
        max_dmg = self.damage + 5
        return random.randint(min_dmg, max_dmg)
