import random
import itertools
from typing import List
from termcolor import colored, cprint
import json

filePath = "mnemonica.txt"
dictionary_path = "fr.json"


class Card:
    def __init__(self, suit: str, value: str) -> None:
        self.value = value
        self.suit = suit

        black_suits = ["C", "S", "clubs", "spades"]
        red_suits = ["H", "D", "hearts", "diamonds"]
        if suit in black_suits:
            self.color = "black"
        elif suit in red_suits:
            self.color = "red"

    def spell(self):
        with open(dictionary_path) as json_file:
            json_file = json.load(json_file)
            json_values = json_file["values"]
            json_suits = json_values["suits"]

            card_value = json_values[self.value]
            card_suit = json_suits[self.suit]

            spell_outs = [f"{card_value}{card_suit}", f"{card_value} {card_suit}"]
            return spell_outs

    def __repr__(self) -> str:
        if self.suit in ["spades", "S"]:
            suit = '♠'
            return colored(f"{self.value}{suit}", 'blue')
        if self.suit in ["clubs", "C"]:
            suit = '♣'
            return colored(f"{self.value}{suit}", 'green')
        if self.suit in ["hearts", "H"]:
            suit = '♥'
            return colored(f"{self.value}{suit}", 'red')
        if self.suit in ["diamonds", "D"]:
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
                positions.append(card_tuple)
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
            # deck += f"{repr(card)} \n"
            deck += f"{position}: {repr(card)} \n"
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


def get_spelling_outs(cards):
    dictionary_path = "fr.json"
    with open(dictionary_path) as json_file:
        data = json.load(json_file)
        values = data["values"]
        suits = data["suits"]
        for card in cards:
            card_index = cards.index(card) + 1
            card_value_in_letters = values[card.value]
            card_suit_in_letters = suits[card.suit]
            card_letters = len(card_suit_in_letters) + len(card_value_in_letters)
            card_letters_with_pronoun = card_letters + 2
            if card_index == card_letters:
                print(f"{card} {card_value_in_letters} {card_suit_in_letters} (on)")
                break
            if card_index == card_letters_with_pronoun:
                print(f"{card} {card_value_in_letters} DE {card_suit_in_letters} (on)")
            if card_index == card_letters + 1:
                print(f"{card} {card_value_in_letters} {card_suit_in_letters} (next)")
            if card_index == card_letters_with_pronoun + 1:
                print(f"{card} {card_value_in_letters} DE {card_suit_in_letters} (next)")

            if card_index == card_letters + 2:
                print(f"{card} {card_value_in_letters} {card_suit_in_letters} (double)")
            if card_index == card_letters_with_pronoun + 2:
                print(f"{card} {card_value_in_letters} DE {card_suit_in_letters} (double)")


deck = build_deck_from_file(filePath)
print(deck)
# for _ in range(8):
#     print(".........................")
#     get_spelling_outs(deck.cards)
#     deck.faro()
# get_spelling_outs(deck.cards)
