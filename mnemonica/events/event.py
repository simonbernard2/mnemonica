import abc

from mnemonica.deck.deck import Deck


class Event(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def apply(self, deck: Deck) -> None:
        pass

    @abc.abstractmethod
    def params(self) -> str:
        pass
