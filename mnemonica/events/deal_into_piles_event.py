import random
from mnemonica.deck.deck import Deck
from mnemonica.events.event import Event


class DealIntoPilesEvent(Event):
    def __init__(self) -> None:
        self.nb_piles = random.randint(2, 5)
        self.nb_cards = random.randint(1, 10)

    def apply(self, deck: Deck) -> None:
        piles = deck.deal_into_piles(self.nb_piles, self.nb_cards)
        deck.reassemble_left_to_right_on_top(piles)

    def params(self) -> str:
        return f"[DealIntoPiles] nb_piles: {self.nb_piles} | nb_cards: {self.nb_cards}]"
