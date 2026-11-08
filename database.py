from tinydb import TinyDB, Query

DB_FILE = "eldoria_save.json"


def get_db():
    return TinyDB(DB_FILE)


def find_account(username):
    db = get_db()
    result = db.table("accounts").get(Query().username == username)
    db.close()
    return result


def create_account(username, password_hash, player_data):
    db = get_db()
    accounts = db.table("accounts")
    if accounts.get(Query().username == username):
        db.close()
        return False
    accounts.insert({"username": username, "password_hash": password_hash, "player": player_data})
    db.close()
    return True


def save_player(username, player_data):
    db = get_db()
    db.table("accounts").update({"player": player_data}, Query().username == username)
    db.close()


def update_password_hash(username, password_hash):
    db = get_db()
    db.table("accounts").update({"password_hash": password_hash}, Query().username == username)
    db.close()
