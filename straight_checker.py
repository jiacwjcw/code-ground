from functools import reduce


def straight_checker(input: str):
    RANKS = {"J": 11, "Q": 12, "K": 13, "A": 14}
    deck = input.split(",")
    sorted(deck)

    for i in range(len(deck)):
        deck[i] = RANKS[deck[i]] if deck[i] in RANKS.keys() else int(deck[i])

    return reduce(lambda x, y: y - x, deck) == deck[2]


def test():
    assert straight_checker("1,2,3,4,5") == True
    assert straight_checker("10,J,Q,K,A") == True
    assert straight_checker("1,3,5,6,8") == False
    assert straight_checker("6,5,3,4,2") == True
    assert straight_checker("J,K,Q,10,9") == True
