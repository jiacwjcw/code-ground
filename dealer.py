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

        self.cards = [f"{suite}{card_type}" for suite in self.suites for card_type in self.card_types]


class Dealer:
    def __init__(self) -> None:
        self.__poker = Poker()
        self.cards = self.__poker.cards

    def deal(self, decks: int = 4):
        should_dealed_count = len(self.cards) // decks
        for i in range(decks):
            a_deck_of_card = []
            for _ in range(should_dealed_count):
                card = random.choice(self.cards)
                a_deck_of_card.append(card)
                self.cards.remove(card)

            print(f"第 {i+1} 副牌組: {a_deck_of_card}")

        print(f"不夠發的牌: {self.cards}")


def main():
    Dealer().deal()
    Dealer().deal(10)


if __name__ == "__main__":
    main()