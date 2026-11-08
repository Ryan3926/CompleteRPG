import random
from colorama import Fore, Style, init
from player import Player
from combat import fight
from inventory import show_inventory, use_item
from npc import talk_to_npc
from shop import visit_shop
from quest import show_quests
from world_map import show_map
from database import save_player

init(autoreset=True)


class Game:
    def __init__(self, username, player_data):
        self.username = username
        self.player = Player(player_data, username)
        self.running = True

    def save(self):
        save_player(self.username, self.player.to_dict())
        print(Fore.GREEN + "Game progress saved.")

    def travel(self):
        destinations = {"1": "Village", "2": "Whispering Woods", "3": "Crystal Caverns", "4": "Ruined Citadel"}
        print("\nTravel: 1. Village  2. Whispering Woods  3. Crystal Caverns  4. Ruined Citadel")
        choice = input("Choose destination: ").strip()
        if choice not in destinations:
            print("Invalid destination.")
            return
        destination = destinations[choice]
        step = self.player.quests.get("main_step", 0)
        if destination == "Crystal Caverns" and step < 2:
            print("The cavern path is sealed. Complete the woods quest first.")
            return
        if destination == "Ruined Citadel" and step < 3:
            print("The Citadel gate is sealed. Defeat the Cave Troll first.")
            return
        self.player.location = destination
        show_map(destination)
        print(f"You travel to {destination}.")

    def explore(self):
        location = self.player.location
        if location == "Village":
            print("The Village is safe. Talk to NPCs, visit the shop, or travel to another area.")
            return
        if location == "Ruined Citadel":
            if self.player.quests.get("main_step", 0) < 3:
                print("The Shadow King's chamber remains sealed.")
                return
            result = fight(self.player, "The Shadow King")
            if result == "won":
                self.player.quests["main_step"] = 4
                print(Fore.MAGENTA + "\nTHE SHADOW KING HAS FALLEN! Eldoria is saved. YOU WIN!")
                self.save()
                self.running = False
            return
        if location == "Whispering Woods" and self.player.quests.get("main_step", 0) == 1:
            result = fight(self.player, "Goblin")
            if result == "won":
                self.player.quests["main_step"] = 2
                print(Fore.GREEN + "Quest complete! The road to Crystal Caverns is open.")
            return
        if location == "Crystal Caverns" and self.player.quests.get("main_step", 0) == 2:
            result = fight(self.player, "Cave Troll")
            if result == "won":
                self.player.quests["main_step"] = 3
                print(Fore.GREEN + "Quest complete! The Ruined Citadel is now accessible.")
            return
        monster = random.choice(["Goblin", "Dire Wolf", "Skeleton", "Cave Troll"])
        fight(self.player, monster)

    def menu(self):
        print(Fore.CYAN + "\n=== ADVENTURER MENU ===")
        print("1. Explore current location")
        print("2. Travel / view map")
        print("3. Talk to NPC")
        print("4. Visit shop / learn skills")
        print("5. View inventory")
        print("6. Use item")
        print("7. View character progress")
        print("8. View quests")
        print("9. Save and continue")
        print("10. Save and quit")

    def run(self):
        print(Fore.YELLOW + f"\nWelcome, {self.player.name}. Your journey begins in the Village.")
        while self.running:
            self.menu()
            choice = input("Choose an option: ").strip()
            if choice == "1":
                self.explore()
            elif choice == "2":
                self.travel()
            elif choice == "3":
                if self.player.location == "Village":
                    talk_to_npc(self.player)
                else:
                    print("No villagers are here. Travel to the Village to speak with them.")
            elif choice == "4":
                if self.player.location == "Village":
                    visit_shop(self.player)
                else:
                    print("The shop is only available in the Village.")
            elif choice == "5":
                show_inventory(self.player)
            elif choice == "6":
                use_item(self.player)
            elif choice == "7":
                self.player.show_status()
            elif choice == "8":
                show_quests(self.player)
            elif choice == "9":
                self.save()
            elif choice == "10":
                self.save()
                print("Your progress is safe. See you next time!")
                self.running = False
            else:
                print(Fore.YELLOW + "Invalid option. Enter a number from 1 to 10.")
        save_player(self.username, self.player.to_dict())
