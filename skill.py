class Skill:
    def __init__(self, name, cooldown):
        self.name = name
        self.cooldown = cooldown

    def use(self, player, monster=None):
        raise NotImplementedError("Each skill subclass must define its own effect.")


class PowerStrike(Skill):
    def __init__(self):
        super().__init__("Power Strike", 1)

    def use(self, player, monster=None):
        damage = 22 + player.level * 3
        monster.take_damage(damage)
        return damage


class Fireball(Skill):
    def __init__(self):
        super().__init__("Fireball", 2)

    def use(self, player, monster=None):
        damage = 30 + player.level * 4
        monster.take_damage(damage)
        print("A burst of flame engulfs the enemy!")
        return damage


class Heal(Skill):
    def __init__(self):
        super().__init__("Heal", 3)

    def use(self, player, monster=None):
        amount = min(35, player.max_hp - player.hp)
        player.hp += amount
        print(f"Healing light restores {amount} HP.")
        return amount


SKILL_CLASSES = {"Power Strike": PowerStrike, "Fireball": Fireball, "Heal": Heal}
SKILL_COSTS = {"Fireball": 40, "Heal": 55}


def learn_skill(player):
    available = [name for name in SKILL_COSTS if name not in player.skills]
    if not available:
        print("You have learned every available skill.")
        return
    print("Learnable skills:")
    for name in available:
        print(f"- {name}: {SKILL_COSTS[name]} gold")
    choice = input("Which skill do you want to learn? (Enter to cancel): ").strip().title()
    if choice not in available:
        print("Cancelled or invalid skill.")
    elif player.gold < SKILL_COSTS[choice]:
        print("You do not have enough gold.")
    else:
        player.gold -= SKILL_COSTS[choice]
        player.skills.append(choice)
        print(f"You learned {choice}!")
