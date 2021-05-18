import unittest

from mnemonica.deck.card import Values, Suits, Card
from mnemonica.deck.deck import Deck
import tests.utils.generate_decks as F
from mnemonica.deck.findings import FlushFound


class TestDeck(unittest.TestCase):
    def test_is_empty_true(self) -> None:
        deck = F.empty_deck()

        self.assertTrue(deck.is_empty())

    def test_is_empty_false(self) -> None:
        deck = F.reversed_deck()

        self.assertFalse(deck.is_empty())

    def test_eq_true(self) -> None:
        deck = F.new_deck()
        same_deck = F.new_deck()

        self.assertTrue(deck == same_deck)
        self.assertTrue(deck == deck)
        self.assertTrue(Deck([]) == Deck([]))

    def test_eq_false(self) -> None:
        deck = F.new_deck()
        other_deck = F.reversed_deck()
        empty_deck = Deck([])
        different_type = "ok"

        self.assertFalse(deck == other_deck)
        self.assertFalse(deck == empty_deck)
        self.assertFalse(deck == different_type)

    # Flaky test, it can fail if the shuffle results in the original order
    def test_shuffle(self) -> None:
        original = F.new_deck()
        shuffled = F.new_deck()

        shuffled.shuffle()

        self.assertFalse(original == shuffled)

    def test_deal_into_piles(self) -> None:
        deck = F.spades_in_order()
        expected = [
            Deck([Card(Values.ACE, Suits.SPADES), Card(Values.FOUR, Suits.SPADES), Card(Values.SEVEN, Suits.SPADES)]),
            Deck([Card(Values.TWO, Suits.SPADES), Card(Values.FIVE, Suits.SPADES), Card(Values.EIGHT, Suits.SPADES)]),
            Deck([Card(Values.THREE, Suits.SPADES), Card(Values.SIX, Suits.SPADES), Card(Values.NINE, Suits.SPADES)]),
        ]

        actual = deck.deal_into_piles(3, 3)

        self.assertEqual(actual, expected)

    def test_find_flushes(self) -> None:
        deck = F.new_deck()
        expected = [
            FlushFound(0, F.clubs_in_order().cards),
            FlushFound(13, F.hearts_in_order().cards),
            FlushFound(26, F.spades_in_order().cards),
            FlushFound(39, F.diamonds_in_order().cards),
        ]

        actual = deck.find_flushes(5)

        self.assertEqual(f"{expected}", f"{actual}")
