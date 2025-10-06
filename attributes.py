# The Cards.py class utilize these dicts as tuples within its constructor.

RANKS: dict[int, str] = {
    # Define Ranks as Dict with rank int as Key and rank name as Value
    # Ace is defined twice; once as 1 and once as 14, for games where the Ace is the High Card
    1: "Ace",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Jack",
    12: "Queen",
    13: "King",
    14: "Ace",
}

SUITS: dict[str, str] = {
    # Define Suits as Dict with suit name as Key and suit unicode as Value
    "Hearts": "\u2665",
    "Spades": "\u2660",
    "Diamonds": "\u2666",
    "Clubs": "\u2663",
}
