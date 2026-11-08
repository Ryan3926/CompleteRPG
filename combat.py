import random
from monster import create_monster
from skill import SKILL_CLASSES
from inventory import use_item


def fight(player, monster_name=None):
    monster = create_monster(monster_name)
    print(f"\nA {monster.name} appears! ({monster.hp} HP)")
    while player.hp > 0 and monster.hp > 0:
        for skill_name in list(player.cooldowns):
            if player.cooldowns[skill_name] > 0:
                player.cooldowns[skill_name] -= 1
        print("\n1. Attack  2. Use skill  3. Use item  4. Try to flee")
        choice = input("Choose an action: ").strip()
        if choice == "1":
            weapon_bonus = 5 if "Iron Blade" in player.inventory else 0
            damage = random.randint(8, 13) + player.level * 2 + weapon_bonus
            monster.take_damage(damage)
        elif choice == "2":
            print("Known skills: " + ", ".join(player.skills))
            name = input("Skill name (Enter to cancel): ").strip().title()
            if name not in player.skills or name not in SKILL_CLASSES:
                print("You have not learned that skill.")
                continue
            if player.cooldowns.get(name, 0) > 0:
                print(f"{name} is on cooldown for {player.cooldowns[name]} more turn(s).")
                continue
            skill = SKILL_CLASSES[name]()
            skill.use(player, monster)
            player.cooldowns[name] = skill.cooldown
        elif choice == "3":
            use_item(player)
            continue
        elif choice == "4":
            if monster.name == "The Shadow King":
                print("You cannot flee from the final battle!")
                continue
            if random.random() < 0.65:
                print("You escaped safely.")
                return "fled"
            print("You failed to escape!")
        else:
            print("Please enter 1, 2, 3, or 4.")
            continue
        if monster.hp <= 0:
            break
        monster.attack_player(player)
    if player.hp <= 0:
        if "Phoenix Feather" in player.inventory:
            player.inventory.remove("Phoenix Feather")
            player.hp = min(40, player.max_hp)
            print("Your Phoenix Feather revives you! You escape the battle.")
            return "revived"
        player.hp = max(1, player.max_hp // 2)
        player.location = "Village"
        print("You were defeated and rescued by a village healer. You wake in the Village with half HP.")
        return "lost"
    gold, drop = monster.rewards()
    player.gold += gold
    player.gain_xp(monster.xp_reward)
    player.monsters_defeated += 1
    print(f"You defeated {monster.name} and found {gold} gold!")
    if drop:
        player.inventory.append(drop)
        print(f"The monster dropped: {drop}")
    return "won"
