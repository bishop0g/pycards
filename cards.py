class Card:
    """
    Defines Card objects.
    Return types:
        __str__: "{RANK} of {SUIT}"
        icon: "{rank value as char}{suit Unicode character}" or "{playing card Unicode character}"
        card_id: "{rank value as char}{suit name as char}

    """

    def __init__(self, rank: tuple[int, str], suit: tuple[str, str]):
        """
        Constructs Cards based on available RANK and SUIT enums, sets Cards.faceup to False by default
        """
        # Assign rank value from key of RANKS dict' tuple
        self.rank_int: int = rank[0]
        # Assign rank name from value of RANKS dict' tuple
        self.rank_name: str = rank[1]
        # Assign suit name from key of SUITS dict' tuple
        self.suit_name: str = suit[0]
        # Assign suit unicode icon from value of SUITS dict' tuple
        self.suit_icon: str = suit[1]
        # Set faceup variable for each card to False automatically
        self.faceup: bool = False

    def flip_face(self) -> None:
        """
        All new Cards are marked as faceup == False by default, which controls how each str method of Card outputs. This means any dealing/list.pop/in-and-out methods within Deck need to include flip_face() for toggling the card face when in play; otherwise, cards are "visible" upon being dealt to tableaus, etc.
        """
        self.faceup = not self.faceup

    def __str__(self) -> str:  # pyright: ignore[reportImplicitOverride]
        """
        Returns as "Rank of Suit"
        """
        if not self.faceup:
            return "??? of ???"
        else:
            return f"{self.rank_name} of {self.suit_name}"

    def icon(self) -> str:
        """
        Returns Card as "#@", where # is a single-char representation of the Rank, and @ is the Unicode icon via suit_icon.
        """
        rank_str: str
        if not self.faceup:
            return "\U0001f0a0"
        else:
            # Sets rank_str to either 2-9, T(en), J(ack), Q(ueen), K(ing), or (Ace), depending on rank_int
            match self.rank_int:
                case (
                    1 | 14
                ):  # 14 is present for cases/games when the Ace's rank_int value is re-assigned as "the High Card"
                    rank_str = "A"
                case 10:
                    rank_str = "T"
                case 11:
                    rank_str = "J"
                case 12:
                    rank_str = "Q"
                case 13:
                    rank_str = "K"
                # Catch-all: set to rank_int
                case _:
                    rank_str = str(self.rank_int)
        return f"{rank_str}{self.suit_icon}"

    def card_id(self) -> str:
        """
        Returns Card as "#&", where # is the first character from the .icon() method, and & is the first letter of the suit_name.
        """
        if not self.faceup:
            return "??"
        else:
            return f"{self.icon()[:1]}{self.suit_name[:1]}"
