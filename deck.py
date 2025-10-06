import random
from .cards import Card
from .attributes import RANKS, SUITS


class Deck:
    """
    Manages creating List of Cards, shuffling and dealing, etc.
    """

    def __init__(self) -> None:
        self.deck: list[Card] = list()

    # Didn't copy this from a tutorial!!!
    # The .items() method converts each key/value from SUITS and RANKS into tuples that Card.__init__ accepts for self.variable assignment. Really cool way to keep the Suits' names and unicodes, and the Ranks' names and ints, iterated together without overcomplication
    def new_deck(self) -> list[Card]:
        self.deck.clear()
        for suit in SUITS.items():
            for rank in RANKS.items():
                self.deck.append(Card(rank, suit))

        return self.deck

    def print_deck(self) -> None:
        for card in self.deck:
            print(f"{card}: {Card.icon(card)}")

    def deal_one(self) -> Card:
        card = self.deck.pop()
        card.flip_face()
        print(f"Card dealt: {card}")
        return card

    def return_one(self, card: Card) -> None:
        card.flip_face()
        self.deck.insert(0, card)

    def shuffle(self) -> None:
        random.shuffle(self.deck)
