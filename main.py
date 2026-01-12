from weapon import Weapon
from hero import Hero
from monster import Monster
from medkit import Medkit


def main():
    excalibur = Weapon("Excalibur", 25)
    hero = Hero("Arthur", 100)
    hero.equip(excalibur)

    loot_item = Medkit("Super Medkit", 50)

    beast = Monster("The Beast", 100, 15, loot = loot_item)

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
        print(f"\n{hero.name}: {hero.get_hp()} HP | {beast.name}: {beast.get_hp()} HP")
        print("OPTIONS: 1. Attack 2. Inventory 3. Run")

        choice = input("Your Move: ")

        if choice == "1":
            print(f"\n> {hero.name} attacks!")
            hero.attack(beast)

            if beast.get_hp() == 0:
                print(f"--> You defeated {beast.name}!")
                break

            print(f"\n> {beast.name} attacks back!")
            beast.attack(hero)

        elif choice == "2":
            hero.view_inventory()

            if len(hero.inventory) > 0:
                print("Type item number to use it (or 0 to cancel)")
                try:
                    item_choice = int(input("> "))

                    if item_choice == 0:
                        print("Cancelled.")

                    elif 1 <= item_choice <= len(hero.inventory):

                        item_to_use = hero.inventory[item_choice - 1]

                        if isinstance(item_to_use, Medkit):
                            hero.heal(item_to_use.healing_amount)
                            hero.inventory.pop(item_choice - 1)
                            print(f"Used {item_to_use.name}!")

                            print(f"\n> {beast.name} attacks while you heal!")
                            beast.attack(hero)

                        elif isinstance(item_to_use, Weapon):
                            hero.equip(item_to_use)
                            print(f"Equipped {item_to_use.name}!")

                            print(f"\n> {beast.name} attacks while you switch gear!")
                            beast.attack(hero)

                    else:
                        print("Invalid item number.")

                except ValueError:
                    print("Please type a valid number.")

        elif choice == "3":
            print("You ran away like a coward!")
            break

        else:
            print("Invalid command! Type 1, 2, or 3")

    if hero.get_hp() > 0:
        print("The Hero Wins! 🏆")

        if beast.loot:
            print(f"You found loot: {beast.loot.name}")
            hero.add_item(beast.loot)
            hero.view_inventory()

    else:
        print("The Monster Wins! ☠️")


if __name__ == "__main__":
    main()