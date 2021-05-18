import unittest
from mnemonica.deck.card import Card, Suits, Values, Value


class TestCard(unittest.TestCase):
    def test_has_same_value_true(self) -> None:
        card = Card(Values.THREE, Suits.HEARTS)
        other = Card(Values.THREE, Suits.DIAMONDS)

        self.assertTrue(card.has_same_value(other))

    def test_has_same_value_false(self) -> None:
        card = Card(Values.TEN, Suits.HEARTS)
        other = Card(Values.SEVEN, Suits.HEARTS)

        actual = card.has_same_value(other)

        self.assertFalse(actual)

    def test_has_same_suit_true(self) -> None:
        card = Card(Values.TEN, Suits.HEARTS)
        other = Card(Values.SEVEN, Suits.HEARTS)

        actual = card.has_same_suit(other)

        self.assertTrue(actual)

    def test_has_same_suit_false(self) -> None:
        card = Card(Values.TEN, Suits.HEARTS)
        other = Card(Values.TEN, Suits.SPADES)

        actual = card.has_same_suit(other)

        self.assertFalse(actual)

    def test_eq_true(self) -> None:
        card = Card(Values.TEN, Suits.HEARTS)
        same_card = Card(Values.TEN, Suits.HEARTS)
        same_card_two = Card(Value(10), Suits.HEARTS)

        self.assertTrue(card == card)
        self.assertTrue(card == same_card)
        self.assertTrue(card == same_card_two)

    def test_eq_false(self) -> None:
        card = Card(Values.TEN, Suits.HEARTS)
        same_value_different_suit = Card(Values.TEN, Suits.DIAMONDS)
        same_suit_different_value = Card(Values.SIX, Suits.HEARTS)
        different_type = 10

        self.assertFalse(card == same_value_different_suit)
        self.assertFalse(card == same_suit_different_value)
        self.assertFalse(card == different_type)
