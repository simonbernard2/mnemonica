import random
import itertools
from typing import List, Tuple
from mnemonica.deck.findings import PairFound, ThreeOfAKindFound, FourOfAKindFound, FlushFound
from mnemonica.deck.card import Card, Suit, Clubs, Hearts, Spades, Diamonds


class Deck:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self) -> Card:
        return self.cards.pop(0)

    def bottom_deal(self) -> Card:
        return self.cards.pop()

    def faro(self) -> None:
        top_half = self.cards[:-26]
        bottom_half = self.cards[26:]
        self.cards = list(itertools.chain(*zip(top_half, bottom_half)))

    def cut_cards(self, number: int) -> 'Deck':
        cut = self.cards[:number]
        self.cards = self.cards[number:]

        return Deck(cut)

    def complete_cut(self, number: int) -> None:
        cut = self.cards[:number]
        self.cards = self.cards[number:] + cut

    def deal_into_piles(self, nb_piles: int, nb_cards: int) -> List['Deck']:
        piles = [[] for _ in range(nb_piles)]

        for _ in range(nb_cards):
            for pile in piles:
                pile.append(self.cards.pop(0))

        return list(map(lambda p: Deck(p), piles))

    def reassemble_left_to_right_on_top(self, piles: List['Deck']) -> None:
        assembled = []
        for pile in piles:
            assembled += pile.cards

        self.cards = assembled + self.cards

    def reassemble_left_to_right_on_bottom(self, piles: List['Deck']) -> None:
        assembled = []
        for pile in piles:
            assembled += pile.cards

        self.cards += self.cards

    def riffle_shuffle(self, deck: 'Deck') -> 'Deck':
        assembled = []
        random_value = random.randint(1, 2)
        first_half = self.cards if random_value == 1 else deck.cards
        second_half = self.cards if random_value == 2 else deck.cards
        while len(first_half) > 0 or len(second_half) > 0:
            random_value = random.randint(1, 5)
            assembled += first_half[0:random_value]
            first_half = first_half[random_value:]

            random_value = random.randint(1, 5)
            assembled += second_half[0:random_value]
            second_half = second_half[random_value:]

        self.cards = assembled
        return self

    def locate_card_by_value(self, value: str) -> List[Tuple[Card, int]]:
        cards = []
        for card in self.cards:
            if value == card.value:
                card_tuple = (card, self.cards.index(card) + 1)
                cards.append(card_tuple)
        return cards

    def locate_card_by_suit(self, suit: str) -> List[Tuple[Card, int]]:
        cards = []
        for card in self.cards:
            if suit == card.suit:
                card_tuple = (card, self.cards.index(card) + 1)
                cards.append(card_tuple)
        return cards

    def locate_cards_by_color(self, color: str) -> List[Tuple[Card, int]]:
        positions = []
        for card in self.cards:
            if card.color == color:
                card_tuple = (card, self.cards.index(card) + 1)
                positions.append(card_tuple)
        return positions

    def find_pairs(self) -> List[PairFound]:
        pairs = []
        for i, card in enumerate(self.cards[:-1]):
            if card.has_same_value(self.cards[i + 1]):
                pairs.append(PairFound(i, (card, self.cards[i + 1])))

        return pairs

    def find_three_of_a_kind(self) -> List[ThreeOfAKindFound]:
        threes = []
        for i, card in enumerate(self.cards[:-2]):
            next_card = self.cards[i + 1]
            second_to_next_card = self.cards[i + 2]
            if card.has_same_value(next_card) and card.has_same_value(second_to_next_card):
                threes.append(ThreeOfAKindFound(i, (card, next_card, second_to_next_card)))

        return threes

    def find_four_of_a_kind(self) -> List[FourOfAKindFound]:
        fours = []
        for i, card in enumerate(self.cards[:-3]):
            next_card = self.cards[i + 1]
            second_to_next_card = self.cards[i + 2]
            third_to_next_card = self.cards[i + 3]
            if card.has_same_value(next_card) and \
                    card.has_same_value(second_to_next_card) and \
                    card.has_same_value(third_to_next_card):
                fours.append(FourOfAKindFound(i, (card, next_card, second_to_next_card, third_to_next_card)))

        return fours

    def find_flush(self, suit: str, minimum_amount: int) -> List[FlushFound]:
        flush: List[FlushFound] = []
        for i, card in enumerate(self.cards):
            if card.suit != suit:
                continue

            position = i+1
            count = 1
            temp_flush = [card]
            if position > len(self.cards)-2:
                break
            print (position)
            next_card = self.cards[i + position]
            while card.has_same_suit(next_card) in enumerate(self.cards):
                count += 1
                temp_flush.append(next_card)
                next_card = self.cards[i + position]

            if len(temp_flush) > len(flush) and len(temp_flush) > minimum_amount:
                position = i
                flush.append(FlushFound(suit, position, temp_flush))

        return flush

    def copy(self) -> 'Deck':
        return Deck(self.cards.copy())

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