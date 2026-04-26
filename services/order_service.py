from services.payment_service import process_payment
from models.order_model import save_order

def process_order(user_id, items):
    payment_status = process_payment(user_id)
    if payment_status:
        return save_order(user_id, items)