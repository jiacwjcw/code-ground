import random


class Poker:
    def __init__(self) -> None:
        self.suites: list = ["♠", "♥", "♦", "♣"]
        self.card_types: list = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
            "A",
        ]

        self.cards = [
            f"{suite}{card_type}"
            for suite in self.suites
            for card_type in self.card_types
        ]


class Dealer:
    def __init__(self) -> None:
        self.__poker = Poker()
        self.cards = self.__poker.cards

    def deal(self, decks: int = 4):
        should_dealed_count = len(self.cards) // decks
        random.shuffle(self.cards)
        for i in range(decks):
            print(
                f"第 {i+1} 副牌組: {self.cards[should_dealed_count*i:should_dealed_count*(i+1)]}"
            )


def main():
    Dealer().deal()


if __name__ == "__main__":
    main()
