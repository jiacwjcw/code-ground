def is_contains7(n: int) -> bool:
    x = n
    while x > 0:
        if x % 10 == 7:
            return True
        x = x // 10
    return False


def containing_seven(n: int) -> int:
    count = 0
    if n < 7:
        return 0
    for i in range(1, n + 1):
        if is_contains7(i):
            count += 1
    return count


def test():
    assert containing_seven(7) == 1  # 1 - 7 之中只有 7 這個數字有 7，所以回傳 1 (個)
    assert containing_seven(20) == 2  # 1 - 20 之中有 7 跟 17 這兩個數字有 7 ，所以回傳 2 (個)
    assert (
        containing_seven(70) == 8
    )  # 1 - 70 之中有 7, 17, 27, 37, 47, 57, 67, 70 這些數字有 7 ，所以回傳 8 (個)
    assert (
        containing_seven(100) == 19
    )  # 1 - 100 之中有 7, 17, 27, 37, 47, 57, 67, 70-79, 87, 97 這些數字有 7 ，所以回傳 19 (個)
    assert containing_seven(pow(10, 3)) == 271
    assert containing_seven(pow(10, 7)) == 5217031
