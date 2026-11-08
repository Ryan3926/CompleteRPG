from item import ITEMS


def show_inventory(player):
    print("\n--- INVENTORY ---")
    if not player.inventory:
        print("Your inventory is empty.")
        return
    counts = {}
    for item in player.inventory:
        counts[item] = counts.get(item, 0) + 1
    for name, count in counts.items():
        print(f"{name} x{count}")


def use_item(player):
    show_inventory(player)
    if not player.inventory:
        return
    name = input("Which item do you want to use? (Enter to cancel): ").strip()
    if not name:
        return
    if name not in player.inventory:
        print("You do not have that item.")
        return
    item = ITEMS.get(name)
    if not item:
        print("That item cannot be used right now.")
        return
    if item["type"] == "healing":
        if player.hp >= player.max_hp:
            print("Your HP is already full.")
            return
        restored = min(item["power"], player.max_hp - player.hp)
        player.hp += restored
        player.inventory.remove(name)
        print(f"You restored {restored} HP.")
    elif item["type"] == "revive":
        print("A Phoenix Feather only works when you fall in battle.")
