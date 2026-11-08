NPCS = {
    "Elder Mira": "The Shadow King has returned. Find allies, grow stronger, and follow the old road to the Citadel.",
    "Healer Rowan": "I can help the village, but I need a Small Potion for my medicine shelf.",
    "Blacksmith Bram": "A good blade can turn a desperate fight. Check the shop if you have enough gold.",
    "Archivist Pell": "A skeleton stole a relic from our archive. Bring it back and I will reward you.",
    "Scout Lyra": "The woods are dangerous, and the caverns are worse. Watch your HP and learn skills before the Citadel."
}


def talk_to_npc(player):
    print("\nPeople in the Village:")
    for name in NPCS:
        print(f"- {name}")
    choice = input("Who do you want to talk to? (Enter to cancel): ").strip().title()
    if choice not in NPCS:
        print("That person is not here.")
        return
    print(f"\n{choice}: {NPCS[choice]}")
    if choice == "Elder Mira" and player.quests.get("main_step", 0) == 0:
        print("Main quest updated: defeat a Goblin in the Whispering Woods.")
        player.quests["main_step"] = 1
    elif choice == "Healer Rowan":
        from quest import complete_side_quest
        complete_side_quest(player, "herbal")
    elif choice == "Archivist Pell":
        from quest import complete_side_quest
        complete_side_quest(player, "relic")
