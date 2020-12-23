from mnemonica.deck.deck import Deck
from mnemonica.events.events import Events
from mnemonica.repo.deck_repo import DeckRepo
from pprint import PrettyPrinter

pp = PrettyPrinter()

dr = DeckRepo("resources/mnemonica.txt")
deck: Deck = dr.load()

for _ in range(10):
    d = deck.copy()
    events = Events.generate()
    events.apply(d)

    result = d.find_three_of_a_kind()
    if len(result) > 0:
        print(result)
        print(events.params())
        print()
