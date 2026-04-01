from weapon import Weapon
from hero import Hero
from monster import Monster
from medkit import Medkit
import json
import logging

logging.basicConfig(
    filename = "logbook.log",
    level = logging.INFO,
    format = "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

def save_result(result):
    try:
        with open("stats.json","r") as f:
            stats = json.load(f)
    except FileNotFoundError:
        stats = {"wins": 0, "losses": 0, "ran": 0}

    if result == "Win":
        stats["wins"] += 1
    elif result == "Loss":
        stats["losses"] += 1
    elif result == "Ran":
        stats["ran"] += 1

    with open("stats.json","w") as f:
        json.dump(stats, f)

    logging.info("Progress saved")

def load_stats():
    try:
        with open("stats.json", "r") as f:
            stats = json.load(f)
        print(f"Welcome back, Arthur!")
        print(f"Your Stats:")
        print(f"- Wins: {stats['wins']}")
        print(f"- Losses: {stats['losses']}")
        print(f"- Ran Away: {stats['ran']}")
    except FileNotFoundError:
        print("No stats yet. This is your first game!")

def main():

    load_stats()
    ran_away = False

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

    logging.info(f"Battle Start: {hero.name} vs {beast.name}")

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
            ran_away = True
            break

        else:
            print("Invalid command! Type 1, 2, or 3")

    if ran_away:
        logging.info("Hero ran away like a coward!")
        save_result("Ran")

    else :
        if hero.get_hp() > 0:
            logging.info(f"{hero.name} win against {beast.name}!")
            save_result("Win")

            if beast.loot:
                print(f"You found loot: {beast.loot.name}")
                hero.add_item(beast.loot)
                hero.view_inventory()

        else:
            logging.info(f"{hero.name} has loss")
            save_result("Loss")


if __name__ == "__main__":
    main()