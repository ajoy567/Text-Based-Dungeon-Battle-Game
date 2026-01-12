import random
from character import Character

class Monster(Character):
    def __init__(self, name, hp, bite_strength, loot = None):
        super().__init__(hp)
        self.name = name
        self.bite_strength = bite_strength
        self.loot = loot

    def attack(self, target):

        min_dmg = self.bite_strength - 4
        max_dmg = self.bite_strength + 4

        if min_dmg < 0:
            min_dmg = 0

        actual_damage = random.randint(min_dmg, max_dmg)


        print(f"{self.name} bites widely! (Dmg: {actual_damage})")
        target.take_damage(actual_damage)
