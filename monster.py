from character import Character

class Monster(Character):
    def __init__(self, name, hp, bite_strength, loot = None):
        super().__init__(hp)
        self.name = name
        self.bite_strength = bite_strength
        self.loot = loot

    def attack(self, target):
        print(f"{self.name} bites the enemy!")
        target.take_damage(self.bite_strength)
