import random


class Monster:
    def __init__(self, name, hp, attack, xp_reward, gold_min, gold_max, drops=None):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.xp_reward = xp_reward
        self.gold_min = gold_min
        self.gold_max = gold_max
        self.drops = drops or []

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)
        print(f"{self.name} takes {amount} damage! ({self.hp}/{self.max_hp} HP left)")

    def attack_player(self, player):
        damage = random.randint(max(1, self.attack - 3), self.attack + 3)
        player.hp = max(0, player.hp - damage)
        print(f"{self.name} hits you for {damage} damage. You have {player.hp}/{player.max_hp} HP.")

    def rewards(self):
        return random.randint(self.gold_min, self.gold_max), random.choice(self.drops) if self.drops and random.random() < 0.45 else None


class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", 35, 8, 25, 5, 12, ["Small Potion"])


class Wolf(Monster):
    def __init__(self):
        super().__init__("Dire Wolf", 45, 10, 30, 6, 14, ["Small Potion"])


class Skeleton(Monster):
    def __init__(self):
        super().__init__("Skeleton", 55, 12, 40, 8, 18, ["Small Potion", "Iron Blade"])


class Troll(Monster):
    def __init__(self):
        super().__init__("Cave Troll", 85, 15, 60, 15, 28, ["Large Potion", "Iron Blade"])


class Boss(Monster):
    def __init__(self):
        super().__init__("The Shadow King", 160, 19, 200, 100, 150, ["Phoenix Feather"])


def create_monster(name=None):
    monsters = {"Goblin": Goblin, "Dire Wolf": Wolf, "Skeleton": Skeleton, "Cave Troll": Troll}
    if name == "The Shadow King":
        return Boss()
    if name in monsters:
        return monsters[name]()
    return random.choice(list(monsters.values()))()
