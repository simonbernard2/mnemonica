import unittest
from mnemonica.deck.card import Card, Suits


class TestCard(unittest.TestCase):
    def test_has_same_value_true(self) -> None:
        card = Card(Suits.HEARTS, "3")
        other = Card(Suits.DIAMONDS, "3")

        self.assertTrue(card.has_same_value(other))

    def test_has_same_value_false(self) -> None:
        card = Card(Suits.HEARTS, "10")
        other = Card(Suits.HEARTS, "7")

        actual = card.has_same_value(other)

        self.assertFalse(actual)

    def test_has_same_suit_true(self) -> None:
        card = Card(Suits.HEARTS, "10")
        other = Card(Suits.HEARTS, "7")

        actual = card.has_same_suit(other)

        self.assertTrue(actual)

    def test_has_same_suit_false(self) -> None:
        card = Card(Suits.HEARTS, "10")
        other = Card(Suits.SPADES, "10")

        actual = card.has_same_suit(other)

        self.assertFalse(actual)

    def test_eq_true(self) -> None:
        card = Card(Suits.HEARTS, "10")
        same_card = Card(Suits.HEARTS, "10")

        self.assertTrue(card == card)
        self.assertTrue(card == same_card)

    def test_eq_false(self) -> None:
        card = Card(Suits.HEARTS, "10")
        same_value_different_suit = Card(Suits.DIAMONDS, "10")
        same_suit_different_value = Card(Suits.HEARTS, "6")
        different_type = 10

        self.assertFalse(card == same_value_different_suit)
        self.assertFalse(card == same_suit_different_value)
        self.assertFalse(card == different_type)
