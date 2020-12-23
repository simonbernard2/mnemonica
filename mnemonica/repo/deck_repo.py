from mnemonica.deck.deck import Deck
from mnemonica.deck.card import (
    Card, Suit, Clubs, Spades, Hearts, Diamonds
)


class DeckRepo:
    def __init__(self, path: str):
        self.path = path

    def load(self) -> Deck:
        with open(self.path, 'r') as temp:
            data = temp.read().splitlines()

        cards = []
        for card in data:
            value, suit_str = card.split(":")
            suit = self._suit_from_string(suit_str)
            cards.append(Card(suit, value))

        return Deck(cards)

    def _suit_from_string(self, s: str) -> Suit:
        d = {
            "C": Clubs(),
            "S": Spades(),
            "H": Hearts(),
            "D": Diamonds()
        }

        if s not in d:
            raise RuntimeError("Invalid suit char")

        return d[s]
