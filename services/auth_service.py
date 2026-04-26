from models.user_model import get_user

def authenticate_user(username, password):
    """
    Validates user credentials
    """
    user = get_user(username)
    if user and user["password"] == password:
        return {"status": "success"}
    return {"status": "failed"}