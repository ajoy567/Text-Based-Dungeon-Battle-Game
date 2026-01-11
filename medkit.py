class Medkit:
    def __init__(self, name, healing_amount):
        self.name = name
        self.healing_amount = healing_amount

    def __str__(self):
        return f"[{self.name}: +{self.healing_amount} HP]"

    def __add__(self, other):
        new_amount = self.healing_amount + other.healing_amount
        new_name = f"Combined {self.name} & {other.name}"

        return Medkit(new_name, new_amount)
