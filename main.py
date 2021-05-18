from mnemonica.deck.deck import Deck
from mnemonica.repo.deck_repo import DeckRepo
from mnemonica.events.events import Events
from mnemonica.deck.card import Suits
from pprint import PrettyPrinter

pp = PrettyPrinter()

dr = DeckRepo("resources/mnemonica.txt")
deck: Deck = dr.load()

#print(deck.cards)
#half = deck.cut_cards(25)
#deck.riffle_shuffle(half)
#print(len(deck.cards))
#print(deck.cards)
deck.faro()
print(deck.find_flushes(2))

# for _ in range(10):
#     d = deck.copy()
#     events = Events.generate()
#     events.apply(d)
#
#     result = d.find_three_of_a_kind()
#     if len(result) > 0:
#         print(result)
#         print(events.params())
#         print()
