MAIN_STEPS = [
    "Speak with Elder Mira in the Village.",
    "Defeat a Goblin in the Whispering Woods.",
    "Defeat a Cave Troll in the Crystal Caverns.",
    "Defeat the Shadow King in the Ruined Citadel."
]


def show_quests(player):
    step = player.quests.get("main_step", 0)
    print("\n--- QUESTS ---")
    if step >= len(MAIN_STEPS):
        print("Main Quest: COMPLETE — Eldoria is saved!")
    else:
        print(f"Main Quest ({step + 1}/{len(MAIN_STEPS)}): {MAIN_STEPS[step]}")
    side = player.quests.get("side_completed", [])
    print("Side Quest: Herbal Remedy - " + ("Complete" if "herbal" in side else "Find a Small Potion for Healer Rowan."))
    print("Side Quest: Lost Relic - " + ("Complete" if "relic" in side else "Defeat a Skeleton and recover its relic."))


def complete_side_quest(player, quest_name):
    completed = player.quests.setdefault("side_completed", [])
    if quest_name in completed:
        print("You have already completed that side quest.")
        return
    if quest_name == "herbal" and "Small Potion" in player.inventory:
        player.inventory.remove("Small Potion")
        player.gold += 20
        player.gain_xp(35)
        completed.append("herbal")
        print("Healer Rowan thanks you. Reward: 20 gold and 35 XP!")
    elif quest_name == "relic" and player.monsters_defeated >= 1:
        player.gold += 30
        player.gain_xp(45)
        completed.append("relic")
        print("You return the relic to Archivist Pell. Reward: 30 gold and 45 XP!")
    else:
        print("You do not meet the requirements for that quest yet.")
