from character import Character

class Hero(Character):
    def __init__(self, name, hp):
        super().__init__(hp)
        self.name = name
        self.weapon = None

    def equip(self, weapon_obj):
        self.weapon = weapon_obj

    def attack(self, target):
        if self.weapon is None:
            print("No Weapon! Cannot Attack...")
        else:
            dmg = self.weapon.use_weapon()
            target.take_damage(dmg)