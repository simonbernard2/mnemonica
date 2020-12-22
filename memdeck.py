import random
import itertools
from typing import List
from termcolor import colored, cprint


class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.value = value
        self.suit = suit
        color = ""
        black_suits = ["C", "S"]
        red_suits = ["H", "D"]
        if suit in black_suits:
            color = "black"
        elif suit in red_suits:
            color = "red"
        self.color = color

    def __repr__(self) -> str:
        if self.suit == 'spades' or self.suit == 'S':
            suit = '♠'
            return colored(f"{self.value}{suit}", 'blue')
        if self.suit == 'clubs' or self.suit == 'C':
            suit = '♣'
            return colored(f"{self.value}{suit}", 'green')
        if self.suit == 'hearts' or self.suit == 'H':
            suit = '♥'
            return colored(f"{self.value}{suit}", 'red')
        if self.suit == 'diamonds' or self.suit == 'D':
            suit = '♦'
            return colored(f"{self.value}{suit}", 'magenta')

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.suit == other.suit and self.value == other.value


# ================================================================================================

class Deck:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    # =====================================================================
    # STACK ALTERATION METHODS
    # =====================================================================
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

    # =====================================================================
    # LOCATION METHODS
    # =====================================================================
    def locate_card_by_value(self, value: str) -> [tuple]:
        cards = []
        for card in self.cards:
            if value == card.value:
                card_tuple = (card, self.cards.index(card) + 1)
                cards.append(card_tuple)
        return cards

    def locate_card_by_suit(self, suit: str) -> [tuple]:
        cards = []
        for card in self.cards:
            if suit == card.suit:
                card_tuple = (card, self.cards.index(card) + 1)
                cards.append(card_tuple)
        return cards

    def locate_cards_by_color(self, color: str) -> [tuple]:
        positions = []
        for card in self.cards:
            if card.color == color:
                card_tuple = (card, self.cards.index(card) + 1)
                positions.append(card)
        return positions

    def find_pairs(self):
        pairs = []
        for card in self.cards[:-1]:
            if card.value == self.cards[self.cards.index(card) + 1].value:
                pairs.append({
                    f"{card.value} of {card.suit} and {self.cards[self.cards.index(card) + 1].suit}": self.cards.index(
                        card) + 1})
        return pairs

    def find_threes_of_a_kind(self):
        threes = []
        for card in self.cards[:-2]:
            condition1 = card.value == self.cards[self.cards.index(card) + 1].value
            condition2 = card.value == self.cards[self.cards.index(card) + 2].value
            if condition1 and condition2:
                card_index = self.cards.index(card)
                threes.append([card, self.cards[card_index + 1], self.cards[card_index + 2]])
        return threes

    # =====================================================================
    # "PYTHON"? METHODS
    # =====================================================================
    def __repr__(self) -> str:
        deck = ""
        position = 1
        for card in self.cards:
            deck += f"{repr(card)} \n"
            # deck += f"{position}: {repr(card)} \n"
            position += 1
        return deck

    def __getitem__(self, index) -> Card:
        return self.cards[index - 1]

    def __len__(self) -> int:
        return len(self.cards)

    # ================================================================================================


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
deck.faro()
print(deck.locate_card_by_suit('C'))
