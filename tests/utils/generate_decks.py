from mnemonica.deck.card import Suits, Values, Card
from mnemonica.deck.deck import Deck


def new_deck() -> Deck:
    return Deck([
        Card(v, s)
        for s in Suits.american_order()
        for v in Values.in_order()
    ])


def reversed_deck() -> Deck:
    return Deck([
        Card(v, s)
        for s in Suits.american_order()[::-1]
        for v in Values.in_order()[::-1]
    ])


def empty_deck() -> Deck:
    return Deck([])


def spades_in_order() -> Deck:
    return Deck([
        Card(v, Suits.SPADES) for v in Values.in_order()
    ])


def clubs_in_order() -> Deck:
    return Deck([
        Card(v, Suits.CLUBS) for v in Values.in_order()
    ])


def hearts_in_order() -> Deck:
    return Deck([
        Card(v, Suits.HEARTS) for v in Values.in_order()
    ])


def diamonds_in_order() -> Deck:
    return Deck([
        Card(v, Suits.DIAMONDS) for v in Values.in_order()
    ])
