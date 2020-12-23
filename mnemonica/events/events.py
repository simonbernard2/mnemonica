from typing import List
import random

from mnemonica.deck.deck import Deck
from mnemonica.events.deal_into_piles_event import DealIntoPilesEvent
from mnemonica.events.event import Event
from mnemonica.events.faro_event import FaroEvent


class Events(Event):
    _events_fn = [
        lambda: DealIntoPilesEvent(),
        lambda: FaroEvent()
    ]

    def __init__(self, events: List[Event]) -> None:
        self.events = events

    @classmethod
    def generate(cls) -> 'Events':
        nb_events = random.randint(2, 5)
        events = [random.choice(cls._events_fn)() for _ in range(nb_events)]

        return cls(events)

    def apply(self, deck: Deck) -> None:
        for event in self.events:
            event.apply(deck)

    def params(self) -> str:
        return "\n".join(map(lambda e: e.params(), self.events))
