"""[summary]
輸入
輸入的第一部分為 n+1 行，其中第一行 n 為取得公式的數量，以下為 n 行取得公式。
取得裝備的公式格式如下：[裝備] [金額] [所需裝備1] [所需裝備2]...
輸入的第二部分為 m+1 行，其中第一行 m 為想取得的道具數量，以下 m 行各包含一個字串為道具名稱。

輸出
輸出包含 m 行，每行為各個想購買的道具的總價。
---
Example 1
Input:
3
長劍 350
抗魔斗篷 450
吸魔劍 600 長劍 抗魔斗篷
2
長劍
吸魔劍

Output:
350
1400
"""

products = dict()


def convert_to_int(value):
    return int(value) if value.isdigit() else exit(f"Covert Error: {value}")


def recursive(product: str):
    values = products[product]
    if str(values).isdigit():
        return int(values)
    else:
        count = 0
        for value in values:
            if value.isdigit():
                count += int(value)
            else:
                count += recursive(value)
        return count


def product_setter(lst: list, number: int):
    try:
        for _ in range(number):
            product = lst.pop(0).split(" ")
            products[product[0]] = product[1:] if len(product) > 2 else product[1]
    except IndexError as e:
        exit(f"Formula Error: {product}")


def product_getter(lst: list, number: int):
    for _ in range(number):
        product = lst.pop(0)
        print(recursive(product))


def product_counter(string: str):
    lst = string.split("\n")
    product_number = convert_to_int(lst.pop(0))
    product_setter(lst, product_number)

    shopping_number = convert_to_int(lst.pop(0))
    product_getter(lst, shopping_number)


string = """6
a 100 b b b
b 1 c c
c 1000 d d d d
d 100 e e f
e 200
f 100
6
a
b
c
d
e
f"""

product_counter(string)
