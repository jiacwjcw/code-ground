from ctypes import cdll


def decode_string(string: str) -> str:
    stack = [["", 1]]
    num = ""
    for i in string:
        if i.isnumeric():
            num += i
        elif i == "[":
            stack.append(["", int(num)])
            num = ""
        elif i.isalpha():
            stack[-1][0] += i
        else:
            char, times = stack.pop()
            stack[-1][0] += char * times
    return stack[-1][0]


decode_string("21[abc]3[cd]ef")
