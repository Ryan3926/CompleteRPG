from item import ITEMS
from skill import learn_skill


def visit_shop(player):
    while True:
        print(f"\n--- VILLAGE SHOP (Gold: {player.gold}) ---")
        for name, item in ITEMS.items():
            print(f"{name}: {item['price']} gold - {item['description']}")
        print("1. Buy item  2. Learn a skill  3. Leave shop")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Item name (Enter to cancel): ").strip().title()
            if name not in ITEMS:
                print("That item is not sold here.")
            elif player.gold < ITEMS[name]["price"]:
                print("Not enough gold.")
            else:
                player.gold -= ITEMS[name]["price"]
                player.inventory.append(name)
                print(f"Bought {name}!")
        elif choice == "2":
            learn_skill(player)
        elif choice == "3":
            return
        else:
            print("Please choose 1, 2, or 3.")
