# Solution1:


def move_specific_character_to_last_v1(m: int, value: str):
    """Version 1: queue 解法
    Target: 輸入一個數字x和字符串，將字符串前x位放到最後面。e.g x=3 . str = abcdefg 輸出 ==> defgabc
    """

    if type(m) is not int or type(value) is not str:
        return "No match type!"
    if len(value) < m:
        return "The length of value is less than m"
    elif len(value) == m:
        return value

    queue = []
    value_list = list(value)

    for _ in range(m):
        character = value_list.pop(0)
        queue.append(character)

    return "".join(value_list + queue)


# Solution2:


def move_specific_character_to_last_v2(m: int, value: str):
    """Version 2: 速解
    Target: 輸入一個數字x和字符串，將字符串前x位放到最後面。e.g x=3 . str = abcdefg 輸出 ==> defgabc
    """

    if type(m) is not int or type(value) is not str:
        return "No match type!"
    if len(value) < m:
        return "The length of value is less than m"
    elif len(value) == m:
        return value
    else:
        return value[m:] + value[:m]
