from services.auth_service import authenticate_user

def login(username, password):
    """
    Handles user login request
    """
    return authenticate_user(username, password)