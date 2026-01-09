# File: main.py
from weapon import Weapon
from hero import Hero
from monster import Monster
from medkit import Medkit


def main():
    excalibur = Weapon("Excalibur", 25)
    hero = Hero("Arthur", 100)
    hero.equip(excalibur)
    beast = Monster("The Beast", 100, 15)

    kit1 = Medkit("Bandage", 10)
    kit2 = Medkit("Antibiotics", 15)

    print(f"Found: {kit1}")
    print(f"Found: {kit2}")

    super_kit = kit1 + kit2

    print(f"Crafted: {super_kit}")

    print("\nUsing the new item...")
    hero.heal(super_kit.healing_amount)

    print(f"\n--- BATTLE START: {hero.name} vs {beast.name} ---")

    while hero.get_hp() > 0 and beast.get_hp() > 0:
        print(f"\n{hero.name} attacks!")
        hero.attack(beast)

        if beast.get_hp() == 0:
            break

        print(f"\n{beast.name} attacks back!")
        beast.attack(hero)

    print("\n--- GAME OVER ---")
    if hero.get_hp() > 0:
        print("The Hero Wins! 🏆")
    else:
        print("The Monster Wins! ☠️")


if __name__ == "__main__":
    main()