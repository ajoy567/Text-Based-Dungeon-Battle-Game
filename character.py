from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, hp):
        self.__hp = hp
        self.name = "Unknown"

    def get_hp(self):
        return self.__hp

    def take_damage(self, amount):
        self.__hp -= amount
        if self.__hp <= 0:
            self.__hp = 0
            print(f"--> {self.name} has died!")
        elif self.__hp < 20:
            print(f"--> Critical Hit! {self.name} has {self.__hp} HP left.")
        else:
            print(f"--> {self.name} took damage. Current HP: {self.__hp}")

    def heal(self, amount):
        self.__hp += amount
        print(f"--> Healed for {amount} HP! Current HP: {self.__hp}")

    def __str__(self):
        return f"[{self.name}: {self.__hp} HP]"

    @abstractmethod
    def attack(self, target):
        pass
