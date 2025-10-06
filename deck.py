import random
from .cards import Card
from .attributes import RANKS, SUITS


class Deck:
    """
    Manages creating a new List of Card objects, manages dealing one Card in and out at a time, and manages shuffling.
    """

    def __init__(self, ace_value: str) -> None:
        """
        Initializes Deck as a new List of Cards.
        The .items() method converts each key/value from SUITS and RANKS into tuples that Card.__init__ accepts for self.variable assignment. Really cool way to keep the Suits' names and unicodes, and the Ranks' names and ints, iterated together without overcomplication.
        """
        to_remove: int = 0
        match ace_value:
            case "high":
                to_remove = 1
            case "low":
                to_remove = 14
            case _:
                pass
        self.deck: list[Card]
        for suit in SUITS.items():
            for rank in RANKS.items():
                # If card rank value doesn't equal the Ace that isn't kept, don't add
                if rank[0] != to_remove:
                    self.deck.append(Card(rank, suit))

    def __str__(self) -> str:  # pyright: ignore[reportImplicitOverride]
        """
        Returns Deck object as a str using the Unicode icon for the back of a playing card
        """
        return "\U0001f0a0"

    def print_all(self) -> None:
        """
        Primarily a troubleshooting method to check existing Cards within a Deck: flips face to enable printing, prints, then flips back.
        """
        for card in self.deck:
            card.flip_face()
            print(f"{card}: {Card.icon(card)}")
            card.flip_face()

    def deal_one(self) -> Card:
        """
        Pops one Card out from Deck and flips its face for play, prints for records.
        """
        card = self.deck.pop()
        card.flip_face()
        print(f"Card dealt: {card}")
        return card

    def return_one(self, card: Card) -> None:
        """
        Takes one Card, prints for records, flips face, inserts to top of Deck.
        """
        print(f"Card returned: {card}")
        card.flip_face()
        self.deck.insert(0, card)

    def shuffle(self) -> None:
        """
        Uses "random" package to shuffle order of Cards within Deck list.
        """
        random.shuffle(self.deck)
