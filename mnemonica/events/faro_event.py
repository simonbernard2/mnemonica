from mnemonica.deck.deck import Deck
from mnemonica.events.event import Event


class FaroEvent(Event):
    def apply(self, deck: Deck) -> None:
        deck.faro()

    def params(self) -> str:
        return "[Faro]"
