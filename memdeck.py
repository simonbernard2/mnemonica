import random
import itertools
from typing import List
from termcolor import colored, cprint
import inspect
from collections import Counter


# __eq__ to compare cards with one another
class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        if self.suit == 'spades':
            suit = '♠'
            return colored(f"{self.value}{suit}", 'blue')
        if self.suit == 'clubs':
            suit = '♣'
            return colored(f"{self.value}{suit}", 'green')
        if self.suit == 'hearts':
            suit = '♥'
            return colored(f"{self.value}{suit}", 'red')
        if self.suit == 'diamonds':
            suit = '♦'
            return colored(f"{self.value}{suit}", 'magenta')

    def __eq__(self, other):
        if not isinstance(other, Card):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.suit == other.suit and self.value == other.value


class Deck:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    def shuffle(self) -> "deck":
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop(0)

    def bottom_deal(self) -> Card:
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

    def cut_cards(self, number) -> "packet":
        packet = []
        for n in range(number):
            card = self.deal()
            packet.append(card)
        return packet

    def deal_into_piles(self, cards: int, piles: int):
        piles = [[] for n in range(piles)]

        for _ in range(cards):
            for pile in piles:
                pile.append(self.cards.pop(0))
        return piles

    def find_mates(self, value: str):
        positions = []
        for card in self.cards:
            if value == card.value:
                positions.append(card)
        return positions

    def find_suit(self, suit: str):
        positions = []
        for card in self.cards:
            if suit == card.suit:
                positions.append(card)
        return positions

    def find_color(self, color: str):
        positions = []
        if color == "red":
            for card in self.cards:
                if card.suit == "hearts":
                    positions.append(card)
                if card.suit == "diamonds":
                    positions.append(card)
        if color == "black":
            for card in self.cards:
                if card.suit == "spades":
                    positions.append(card)
                if card.suit == "clubs":
                    positions.append(card)
        return positions

    # Doit ben avoir moyen de simplifier ça? m'semble ça fait du self.cards en esti dans même phrase
    # refere a findMazine
    def find_pairs(self):
        pairs = []
        for card in self.cards[:-1]:
            if card.value == self.cards[self.cards.index(card) + 1].value:
                pairs.append({
                    f"{card.value} of {card.suit} and {self.cards[self.cards.index(card) + 1].suit}": self.cards.index(
                        card) + 1})
        return pairs

    def findMazine(self):
        for i in range(0, len(self.cards) - 1):
            if self.cards[i].value == self.cards[i + 1].value:
                return 0

    # Doit ben avoir moyen de simplifier ça? m'semble ça fait du self.cards en esti dans même phrase
    def find_threes_of_a_kind(self):
        threes = []
        for card in self.cards[:-2]:
            condition1 = card.value == self.cards[self.cards.index(card) + 1].value
            condition2 = card.value == self.cards[self.cards.index(card) + 2].value
            if condition1 and condition2:
                card_index = self.cards.index(card)
                threes.append([card, self.cards[card_index + 1], self.cards[card_index + 2]])
        return threes

    def __repr__(self) -> str:
        deck = ""
        position = 1
        for card in self.cards:
            deck += f"{repr(card)} \n"
            # deck += f"{position}: {repr(card)} \n"
            position += 1
        return deck

    def __len__(self) -> str:
        return len(self.cards)


class Player:
    def __init__(self):
        self.hand = []

    def draw(self, deck, number):
        for i in range(number):
            card = deck.deal()
            self.hand.append(card)
        return


def build_deck_from_file(filePath: str) -> Deck:
    with open(filePath, 'r') as temp:
        data = temp.read().splitlines()

    cards = []
    for card in data:
        value, suit = card.split(":")
        cards.append(Card(suit, value))

    return Deck(cards)


filePath = "mnemonica.txt"
deck = build_deck_from_file(filePath)

card = Card('spades', '5')
#
# user_input = int(input(f"Veuillez inscrire un chiffre entre 1 et 52: "))
# while user_input not in range(1,52):
#     user_input = int(input(f"Veuillez inscrire un chiffre entre 1 et 52: "))
# print(deck.cards[user_input-1]

print(card)
print(deck.cards[15])
print(card == deck.cards[15])
print(card.suit, deck.cards[15].suit)
