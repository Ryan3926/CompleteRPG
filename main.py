from auth import login_or_register
from game import Game


def main():
    print("\n=== SHADOWS OF ELDORIA ===")
    player_data, username = login_or_register()
    if player_data is None:
        print("Goodbye, adventurer!")
        return
    game = Game(username, player_data)
    game.run()


if __name__ == "__main__":
    main()
