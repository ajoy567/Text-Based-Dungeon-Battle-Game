from character import Character

class Monster(Character):
    def __init__(self, name, hp, bite_strength):
        super().__init__(hp)
        self.name = name
        self.bite_strength = bite_strength

    def attack(self, target):
        print(f"{self.name} bites the enemy!")
        target.take_damage(self.bite_strength)