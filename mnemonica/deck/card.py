import abc
from enum import Enum


class Suit(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def icon(self) -> str:
        pass

    @abc.abstractmethod
    def color(self) -> str:
        pass


class Clubs(Suit):
    def icon(self) -> str:
        return "♣"

    def color(self) -> str:
        return "green"


class Spades(Suit):
    def icon(self) -> str:
        return "♠"

    def color(self) -> str:
        return "blue"


class Hearts(Suit):
    def icon(self) -> str:
        return "♥"

    def color(self) -> str:
        return "red"


class Diamonds(Suit):
    def icon(self) -> str:
        return "♦"

    def color(self) -> str:
        return "magenta"


class Color(Enum):
    RED = "red"
    BLACK = "black"


class Card:
    def __init__(self, suit: Suit, value: str) -> None:
        self.value = value
        self.suit = suit

        self.color = Color.RED
        if isinstance(suit, (Clubs, Spades)):
            self.color = Color.BLACK

    # def spell(self):
    #     with open(dictionary_path) as json_file:
    #         json_file = json.load(json_file)
    #         json_values = json_file["values"]
    #         json_suits = json_values["suits"]
    #
    #         card_value = json_values[self.value]
    #         card_suit = json_suits[self.suit]
    #
    #         spell_outs = [f"{card_value}{card_suit}", f"{card_value} {card_suit}"]
    #         return spell_outs

    def has_same_value(self, other: 'Card') -> bool:
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(f"{self.value}-{self.suit.icon()}")

    def __repr__(self) -> str:
        return f"{self.value}{self.suit.icon()}"

    def __eq__(self, other: any) -> bool:
        if not isinstance(other, Card):
            return False

        return hash(self) == hash(other)
