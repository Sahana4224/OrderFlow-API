def check_auth(user):
    """
    Middleware to check if user is authenticated
    """
    return user is not None