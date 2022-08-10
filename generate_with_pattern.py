import re


def check_valid(s: str = ""):
    new_s = ""
    for c in s:
        if c == "{" or c == "}":
            new_s += c
    while "{}" in new_s:
        new_s = new_s.replace("{}", "")
    return new_s == ""


def gen_by_pattern(s: str = ""):
    if not check_valid(s):
        return ""

    pattern = r"([0-9]+||^$)\{([0-9a-z]+)\}"
    m = re.search(pattern, s)

    while m is not None:
        n, c = m.groups()
        n = 1 if not n else n
        c *= int(n)
        s = s[: m.start()] + c + s[m.end() :]
        print(s)
        m = re.search(pattern, s)
        print(m)

    return s


gen_by_pattern("4{1a3}{3}")


def test():
    assert gen_by_pattern("1{2{3}") == ""
    assert gen_by_pattern("1{tv}") == "tv"
    assert gen_by_pattern("{tv}") == "tv"
    assert gen_by_pattern("0{tv}") == ""
    assert gen_by_pattern("1{a3{c}v}") == "acccv"
    assert (
        gen_by_pattern("3{a10{b}3{c}}") == "abbbbbbbbbbcccabbbbbbbbbbcccabbbbbbbbbbccc"
    )
    assert gen_by_pattern("2{4{1a}cc}") == "1a1a1a1acc1a1a1a1acc"
