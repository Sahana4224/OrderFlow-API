from utils.db import save_to_db

def save_order(user_id, items):
    return save_to_db({"user": user_id, "items": items})