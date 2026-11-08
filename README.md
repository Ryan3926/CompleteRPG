# Shadows of Eldoria — Terminal RPG

## Requirements
- Python 3.10+
- `colorama` for colored terminal text
- `tinydb` for local account and save storage

## Setup with uv
From this folder, run:

```bash
uv init --bare
uv add colorama tinydb
uv run main.py
```

If you already have a `pyproject.toml`, simply run `uv add colorama tinydb` and then `uv run main.py`.

You can also use pip:

```bash
python -m pip install colorama tinydb
python main.py
```

## How to play
1. Register a username, password, and character name, or log into an existing account.
2. Talk to Elder Mira in the Village to begin the main quest.
3. Travel to the Whispering Woods and defeat the Goblin.
4. Travel to the Crystal Caverns and defeat the Cave Troll.
5. Prepare in the Village, then travel to the Ruined Citadel and defeat the Shadow King.
6. Complete side quests, buy potions, learn skills, and check your character status along the way.
7. Choose **Save and quit** to save progress in `eldoria_save.json`. Log in again to continue.

## Files
- `main.py`: program entry point
- `game.py`: main game loop, travel, exploration, and menu
- `player.py`: character statistics and leveling
- `monster.py`: base monster and five monster types (inheritance)
- `skill.py`: base skill, skill subclasses, and learning skills (inheritance)
- `combat.py`: turn-based battle logic
- `item.py`: item definitions
- `inventory.py`: inventory display and item use
- `quest.py`: main quest and side quest progress
- `npc.py`: five NPCs and their dialogue
- `shop.py`: buying items and learning skills
- `world_map.py`: different map layouts with walls and obstacles
- `database.py`: TinyDB save/load helpers
- `auth.py`: account registration and login

## Notes
- The local database file `eldoria_save.json` is created automatically.
- This is a class-project demo. Passwords are hashed with SHA-256 for a basic example; production authentication should use a password-specific hashing algorithm such as Argon2 or bcrypt with salts.
- Side quest “Herbal Remedy” is completed by talking to Healer Rowan while carrying a Small Potion. “Lost Relic” becomes available after defeating at least one monster; speak to Archivist Pell to claim the reward.
