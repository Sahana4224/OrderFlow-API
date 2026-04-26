from services.order_service import process_order

def create_order(user_id, items):
    return process_order(user_id, items)