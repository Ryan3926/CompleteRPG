import hashlib
import hmac
from colorama import Fore, Style, init
from database import find_account, create_account
from player import Player

init(autoreset=True)


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def login_or_register():
    print(Fore.CYAN + "\nThe kingdom of Eldoria is fading. Shadows crawl from the Ruined Citadel, and only a new hero can stop the Shadow King.")
    while True:
        print("\n1. Log in  2. Register  3. Quit")
        choice = input("Choose: ").strip()
        if choice == "3":
            return None, None
        if choice not in ("1", "2"):
            print(Fore.YELLOW + "Please enter 1, 2, or 3.")
            continue
        username = input("Username: ").strip()
        password = input("Password: ")
        if not username or not password:
            print(Fore.YELLOW + "Username and password cannot be blank.")
            continue
        account = find_account(username)
        if choice == "2":
            if account:
                print(Fore.RED + "That username already exists.")
                continue
            name = input("Character name: ").strip() or username
            player = Player(username=username)
            player.name = name
            if create_account(username, hash_password(password), player.to_dict()):
                print(Fore.GREEN + "Account created! Welcome to Eldoria.")
                return player.to_dict(), username
        else:
            if account and hmac.compare_digest(account["password_hash"], hash_password(password)):
                print(Fore.GREEN + f"Welcome back, {account['player'].get('name', username)}!")
                return account["player"], username
            print(Fore.RED + "Incorrect username or password.")
