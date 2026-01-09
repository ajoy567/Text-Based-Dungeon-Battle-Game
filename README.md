# Text-Based Dungeon Battle Game

A Python-based command-line RPG game where a hero fights against monsters using weapons and items.

## 🎮 Game Description
This project is a text-based adventure game built with Python. Players control a **Hero** (Arthur) equipped with weapons (like Excalibur) to battle against enemies (like The Beast). The game features a combat system, health management, and an item crafting mechanic for healing.

## ✨ Features
* **Combat System:** Turn-based battles between the Hero and Monsters.
* **Inventory & Equipment:** Equip weapons to increase damage.
* **Item Crafting:** Combine smaller medkits to create a "Super Kit" for better healing.
* **Object-Oriented Design:** Code is structured using classes for Characters, Weapons, and Items.

## 🚀 How to Run
1.  Make sure you have Python installed (Python 3.11 is recommended).
2.  Clone or download this repository.
3.  Run the main game file:

    ```bash
    python main.py
    ```

## 📂 Project Structure
* `main.py`: The entry point of the game; handles the game loop and logic.
* `hero.py`: Defines the Hero class and their abilities.
* `monster.py`: Defines the Monster class and enemy behaviors.
* `weapon.py`: Handles weapon properties like damage and names.
* `medkit.py`: Logic for healing items and crafting mechanics.