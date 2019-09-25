#J'essaie de faire un programme qui simule un jeu de cartes pour faire des recherches sur le memdeck
#test de git
import random
import itertools
from typing import List
import inspect
from collections import Counter


class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
      return f"{self.value} of {self.suit}"

    # def __eq__(self, other): 
    #     if not isinstance(other, Card):
    #     # don't attempt to compare against unrelated types
    #      return NotImplemented

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
    
    def dealIntoPiles(self,cards: int, piles: int):
        piles = [[] for n in range(piles)]

        for _ in range(cards):
            for pile in piles:
                pile.append(self.cards.pop(0))
        return piles
    
    def findMates(self,value:str):
        positions = []
        for card in self.cards:
            if value == card.value:
                positions.append(card)
        return positions

    def findSuit(self, suit:str):
        positions = []
        for card in self.cards:
            if suit == card.suit:
                positions.append(card)
        return positions

    def findColor(self, color:str):
        positions = []
        if color == "red":
            for card in self.cards:
                if card.suit == "hearts":
                    positions.append(card)
                if card.suit == "diamonds":
                    positions.append(card)
        if color == "black":
            for card in self.cards:
                if card.suit == "hearts":
                    positions.append(card)
                if card.suit == "diamonds":
                    positions.append(card)
        return positions

    #Doit ben avoir moyen de simplifier ça? m'semble ça fait du self.cards en esti dans même phrase
    def findPairs(self):
        pairs = []
        for card in self.cards[:-1] :
            if card.value == self.cards[self.cards.index(card)+1].value:
                pairs.append({f"{card.value} of {card.suit} and {self.cards[self.cards.index(card)+1].suit}": self.cards.index(card)+1})
        return pairs
    
    #Doit ben avoir moyen de simplifier ça? m'semble ça fait du self.cards en esti dans même phrase
    def findThreeOfAKind(self):
        threes = []
        for card in self.cards[:-2] :
            if card.value == self.cards[self.cards.index(card)+1].value and card.value == self.cards[self.cards.index(card)+2].value:
                threes.append({f"{card.value} of {card.suit}, {self.cards[self.cards.index(card)+1].suit} and {self.cards[self.cards.index(card)+2].suit}": self.cards.index(card)+1})
        return threes

    def __repr__(self) -> str:
      deck = ""
      i=1
      for card in self.cards:
        deck += f"{i}: " + repr(card) + "\n"
        i += 1

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
      value, suit = card.split(":")

      cards.append(Card(suit, value))
    
    return Deck(cards)
filePath = "mnemonica.txt"
deck = buildDeckFromFile(filePath)



######################################################### COMPARING CARDS ################################################
#comparator 1 (not working)
if deck.cards[0] == Card("clubs","4"):
    print("C1: yes")
else:
    print("C1: no")
#comparator 1.1 (not working)
if deck.cards[0] is Card("clubs","4"):
    print("C1.1: yes")
else:
    print("C1.1: no")

#comparator 2 (not working)
guess = Card("clubs","4")

if deck.cards[0] == guess:
    print("C2: yes")
else:
    print("C2: no")
#comparator 2.2 (not working)

if deck.cards[0] is guess:
    print("C2.2: yes")
else:
    print("C2.2: no")

#comparator 3 (works)

if deck.cards[0].suit == guess.suit and deck.cards[0].value == guess.value:
    print("C3: yes")
else:
    print("C3: no")
#comparator 3.3 
if deck.cards[0].suit == "clubs" and deck.cards[0].value == "4":
    print("C3.1: yes")
else:
    print("C3.1: no")


#I tried both "is" and "==", can't seem to be able to compare "identical" objects without going through their attributes one by one

######################################################### // COMPARING CARDS ################################################



deck.shuffle()
print(deck)
print(deck.findPairs())
print(deck.findThreeOfAKind())

