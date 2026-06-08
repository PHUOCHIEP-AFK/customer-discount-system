from discount import calculate_discount

def test_tc01():
    # 60M + 2M = 62M (>= 50M) => Giảm 10%
    assert calculate_discount(60000000, 2000000) == 0.1

def test_tc02():
    # 30M + 2M = 32M (< 50M) => Không giảm
    assert calculate_discount(30000000, 2000000) == 0

def test_tc03():
    # 49M + 2M = 51M (>= 50M) => Giảm 10%
    assert calculate_discount(49000000, 2000000) == 0.1