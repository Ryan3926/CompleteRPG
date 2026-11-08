ITEMS = {
    "Small Potion": {"price": 10, "description": "Restores 30 HP.", "type": "healing", "power": 30},
    "Large Potion": {"price": 25, "description": "Restores 70 HP.", "type": "healing", "power": 70},
    "Iron Blade": {"price": 40, "description": "A sturdy blade. Adds 5 damage to basic attacks.", "type": "weapon", "power": 5},
    "Phoenix Feather": {"price": 50, "description": "Revives you with 40 HP if you fall in battle.", "type": "revive", "power": 40},
}


def show_item(item_name):
    item = ITEMS.get(item_name)
    if item:
        print(f"{item_name} - {item['description']}")
    else:
        print(f"{item_name} - An unusual item.")
