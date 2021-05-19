from mnemonica.deck.deck import Deck
from mnemonica.repo.deck_repo import DeckRepo
from mnemonica.events.events import Events
from pprint import PrettyPrinter

pp = PrettyPrinter()

# dr = DeckRepo("resources/mnemonica.txt")
dr = DeckRepo("resources/aceToKing.txt")
deck: Deck = dr.load()
#
# card = deck.cards[51]
#
# deck.cull_card(card,1)

hand = deck.cut_cards(5)

print(hand)
print(hand.is_a_flush())

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
