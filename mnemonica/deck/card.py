from typing import List
from enum import Enum


class Suit:
    def __init__(self, icon: str, color: str) -> None:
        self.icon = icon
        self.color = color

    def __eq__(self, other: any) -> bool:
        if not isinstance(other, Suit):
            return False

        return self.icon == other.icon

    def __hash__(self) -> int:
        return hash(f"{self.icon}")


class Value:
    def __init__(self, value: int) -> None:
        self.value = value

    def is_court(self) -> bool:
        return self.value > 10

    def is_spot(self) -> bool:
        return self.value < 11

    def __repr__(self) -> str:
        return f"{self.value}"

    def __eq__(self, other: any) -> bool:
        if not isinstance(other, Value):
            return False

        return self.value == other.value

    def __hash__(self) -> int:
        return hash(f"{self.value}")


class Values:
    ACE = Value(1)
    TWO = Value(2)
    THREE = Value(3)
    FOUR = Value(4)
    FIVE = Value(5)
    SIX = Value(6)
    SEVEN = Value(7)
    EIGHT = Value(8)
    NINE = Value(9)
    TEN = Value(10)
    JACK = Value(11)
    QUEEN = Value(12)
    KING = Value(13)

    @classmethod
    def in_order(cls):
        return [cls.ACE, cls.TWO, cls.THREE, cls.FOUR, cls.FIVE, cls.SIX, cls.SEVEN, cls.EIGHT, cls.NINE, cls.TEN,
                cls.JACK, cls.QUEEN, cls.KING]


class Suits:
    CLUBS = Suit("♣", "green")
    SPADES = Suit("♠", "blue")
    HEARTS = Suit("♥", "red")
    DIAMONDS = Suit("♦", "magenta")

    @classmethod
    def american_order(cls) -> List[Suit]:
        return [cls.CLUBS, cls.HEARTS, cls.SPADES, cls.DIAMONDS]


class Color(Enum):
    RED = "red"
    BLACK = "black"


class Card:
    def __init__(self, value: Value, suit: Suit) -> None:
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
