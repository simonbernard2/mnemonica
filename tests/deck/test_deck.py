import unittest
from mnemonica.deck.deck import Deck
from mnemonica.deck.card import Card, Suit, Suits


class TestDeck(unittest.TestCase):
    def test_is_empty_true(self) -> None:
        deck = Deck([])

        self.assertTrue(deck.is_empty())

    def test_is_empty_false(self) -> None:
        deck = Deck([Card(Suits.HEARTS, "4")])

        self.assertFalse(deck.is_empty())

    def test_eq_true(self) -> None:
        deck = self._all_suit_deck(Suits.HEARTS)
        same_deck = self._all_suit_deck(Suits.HEARTS)

        self.assertTrue(deck == same_deck)
        self.assertTrue(deck == deck)
        self.assertTrue(Deck([]) == Deck([]))

    def test_eq_false(self) -> None:
        deck = self._all_suit_deck(Suits.HEARTS)
        other_deck = self._all_suit_deck(Suits.CLUBS)
        empty_deck = Deck([])
        different_type = "ok"

        self.assertFalse(deck == other_deck)
        self.assertFalse(deck == empty_deck)
        self.assertFalse(deck == different_type)

    # Flaky test, it can fail if the shuffle results in the original order
    def test_shuffle(self) -> None:
        original = self._all_suit_deck(Suits.DIAMONDS)
        shuffled = self._all_suit_deck(Suits.DIAMONDS)

        shuffled.shuffle()

        self.assertFalse(original == shuffled)

    def _all_suit_deck(self, suit: Suit) -> Deck:
        values = ["A"] + [str(i) for i in range(2, 11)] + ["J", "Q", "K"]

        return Deck([Card(suit, v) for v in values])
