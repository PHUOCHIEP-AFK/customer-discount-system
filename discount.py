def calculate_discount(total_spent, new_order_value):
    if total_spent >= 50000000:
        return 0.1
    if total_spent + new_order_value >= 50000000:
        return 0.1
    return 0
