# Define Ranks as Dict with rank int as Key and rank name as Value
RANKS: dict[int, str] = {
    1: "Ace",  # Aces are lowest card for the purposes of this assignment
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
}
# Define Suits as Dict with suit name as Key and suit unicode as Value
SUITS: dict[str, str] = {
    "Hearts": "\u2665",
    "Spades": "\u2660",
    "Diamonds": "\u2666",
    "Clubs": "\u2663",
}
