def calculate_discount(total_spent, new_order_value):
    # Tổng giá trị sau khi thêm đơn hàng hiện tại
    if (total_spent + new_order_value) >= 50000000:
        return 0.1
    else:
        return 0.0