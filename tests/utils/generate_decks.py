from mnemonica.deck.card import Suits, Values, Card, Value
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


def from_string(values: str, sep: str = " ") -> Deck:
    """
    :param values: String representation of a deck
    :param sep: Separator in the values param, defaults to space
    :return: The corresponding deck

    Example:
    from_string("3C 7D")

    Deck([Card(Value.THREE, Suits.CLUBS), Card(Value.SEVEN, Suits.DIAMONDS)])
    """
    cards_as_value_suit_tuple = map(lambda v: (v[:-1], v[-1]), values.split(sep))

    return Deck(
        list(
            map(lambda v_s_tuple: Card(
                Values.from_string(v_s_tuple[0]),
                Suits.from_string(v_s_tuple[1])
            ), cards_as_value_suit_tuple)
        )
    )
