class Player:
    """Stores a player's character stats and progress."""
    def __init__(self, data=None, username="adventurer"):
        data = data or {}
        self.username = username
        self.name = data.get("name", username)
        self.hp = data.get("hp", 100)
        self.max_hp = data.get("max_hp", 100)
        self.xp = data.get("xp", 0)
        self.level = data.get("level", 1)
        self.gold = data.get("gold", 25)
        self.inventory = data.get("inventory", ["Small Potion"])
        self.skills = data.get("skills", ["Power Strike"])
        self.cooldowns = data.get("cooldowns", {})
        self.location = data.get("location", "Village")
        self.quests = data.get("quests", {"main_step": 0, "side_completed": []})
        self.monsters_defeated = data.get("monsters_defeated", 0)

    def gain_xp(self, amount):
        self.xp += amount
        print(f"You gained {amount} XP!")
        while self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level += 1
            self.max_hp += 15
            self.hp = self.max_hp
            print(f"LEVEL UP! You are now level {self.level}. Your HP is restored.")

    def to_dict(self):
        return {
            "name": self.name, "hp": self.hp, "max_hp": self.max_hp,
            "xp": self.xp, "level": self.level, "gold": self.gold,
            "inventory": self.inventory, "skills": self.skills,
            "cooldowns": self.cooldowns, "location": self.location,
            "quests": self.quests, "monsters_defeated": self.monsters_defeated
        }

    def show_status(self):
        print("\n--- CHARACTER STATUS ---")
        print(f"Name: {self.name} | Level: {self.level} | XP: {self.xp}/{self.level * 100}")
        print(f"HP: {self.hp}/{self.max_hp} | Gold: {self.gold}")
        print(f"Skills: {', '.join(self.skills) if self.skills else 'None'}")
        print(f"Location: {self.location} | Monsters defeated: {self.monsters_defeated}")
        print(f"Main quest step: {self.quests.get('main_step', 0)}/4")
