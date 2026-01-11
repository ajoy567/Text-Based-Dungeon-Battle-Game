from character import Character

class Hero(Character):
    def __init__(self, name, hp):
        super().__init__(hp)
        self.name = name
        self.weapon = None
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item}")

    def equip(self, weapon_obj):
        self.weapon = weapon_obj
        print(f"{self.name} equipped {self.weapon.name}!")

    def attack(self, target):
        if self.weapon is None:
            print("No Weapon! Cannot Attack...")
        else:
            dmg = self.weapon.use_weapon()
            target.take_damage(dmg)

    def view_inventory(self):
        print(f"\n--- {self.name}'s Inventory ---")

        if len(self.inventory) == 0:
            print("(Empty)")
        else:
            for index, item in enumerate(self.inventory):
                print(f"{index + 1}. {item.name}")

        print("----------------------------\n")