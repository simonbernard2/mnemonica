#J'essaie de faire un programme qui simule un jeu de cartes pour faire des recherches sur le memdeck
#test de git
import random
import itertools
from typing import List


class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
      return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    def shuffle(self) -> "deck":
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop(0)

    def bottomDeal(self) -> Card:
        return self.cards.pop()
    
    def faro(self) -> 'Deck':
        if len(self.cards) % 2 != 0:
            return False
        else:
            half = len(self.cards) // 2
            topHalf = self.cards[:half]
            bottomHalf = self.cards[half:]
            self.cards = list(itertools.chain(*zip(topHalf, bottomHalf)))
        return self

    def cutCards(self,number) -> "packet":
        packet=[]
        for n in range(number):
            card = self.deal()
            packet.append(card)
        return packet
    
    def dealIntoPiles(self,cards,piles):
        piles = [[] for n in range(piles)]

        for _ in range(cards):
            for pile in piles:
                pile.append(self.cards.pop(0))
        return piles


    def __repr__(self) -> str:
      deck = ""
      for card in self.cards:
        deck += repr(card) + "\n"

      return deck

    def __len__(self) -> str:
      return len(self.cards)
    

class Player:
    def __init__(self):
        self.hand = []

    def draw(self,deck,number):
        for i in range(number):
            card = deck.deal()
            self.hand.append(card)
        return 


def buildDeckFromFile(filePath: str) -> Deck:
    with open(filePath, 'r') as temp:
      data = temp.read().splitlines()
    
    cards = []
    for card in data:
      value, suite = card.split(":")

      cards.append(Card(suite, value))
    
    return Deck(cards)
filePath = "mnemonica.txt"
deck = buildDeckFromFile(filePath)

#coupe 10 cartes
deck.cutCards(10)
#fait un melange faro
deck.faro()
#distribue 6 cartes en 3 paquets
packets = deck.dealIntoPiles(6,3)
print(packets[0])
