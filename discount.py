def calculate_discount(total_spent, new_order_value):
    if (total_spent + new_order_value) >= 50000000:
        return 0.1
    else:
        return 0.0
    