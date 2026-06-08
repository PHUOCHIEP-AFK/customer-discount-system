def calculate_discount(total_spent):
    """
    Hàm tính chiết khấu ban đầu dựa trên 1 tham số tổng số tiền.
    """
    if total_spent >= 50000000:
        return 0.1
    else:
        return 0.0