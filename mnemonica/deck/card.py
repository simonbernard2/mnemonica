from enum import Enum


class Suit:
    def __init__(self, icon: str, color: str) -> None:
        self.icon = icon
        self.color = color


class Suits:
    CLUBS = Suit("♣", "green")
    SPADES = Suit("♠", "blue")
    HEARTS = Suit("♥", "red")
    DIAMONDS = Suit("♦", "magenta")


class Color(Enum):
    RED = "red"
    BLACK = "black"


class Card:
    def __init__(self, suit: Suit, value: str) -> None:
        self.value = value
        self.suit = suit

        self.color = Color.RED
        if suit in (Suits.CLUBS, Suits.SPADES):
            self.color = Color.BLACK

    def has_same_value(self, other: 'Card') -> bool:
        return self.value == other.value

    def has_same_suit(self, other: 'Card') -> bool:
        return self.suit == other.suit

    def __hash__(self) -> int:
        return hash(f"{self.value}-{self.suit.icon}")

    def __repr__(self) -> str:
        return f"{self.value}{self.suit.icon}"

    def __eq__(self, other: any) -> bool:
        if not isinstance(other, Card):
            return False

        return hash(self) == hash(other)
