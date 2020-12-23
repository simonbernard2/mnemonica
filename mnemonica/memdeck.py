import random
import itertools
from typing import List
from termcolor import colored, cprint
import json

filePath = "mnemonica.txt"
dictionary_path = "fr.json"


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
