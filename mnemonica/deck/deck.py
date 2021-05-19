import random
import itertools
from typing import List, Tuple
from mnemonica.deck.findings import PairFound, ThreeOfAKindFound, FourOfAKindFound, FlushFound, StraightFound
from mnemonica.deck.card import Card


class Deck:
    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    def is_empty(self) -> bool:
        return len(self.cards) == 0

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def deal(self) -> Card:
        # FIXME: not working when trying to cull a "card = deck.deal()", but it works when "card = self.cards[index]"
        return self.cards.pop(0)

    def bottom_deal(self) -> Card:
        # FIXME: like mentioned before
        return self.cards.pop()

    def faro(self, other: 'Deck' = None, in_faro=False) -> 'Deck':
        # TODO: settling on which half is which, and stick to this kind of logic all around
        # TODO: rethinking methods where two packets are involved(riffles, comparisons, etc.)...
        # ... and considering cases where it could be done to itself via a cut for instance
        if other:
            top_half, bottom_half = other.cards, self.cards
        else:
            # TODO: considering faros with non 52-cards decks
            top_half = self.cards[:-26]
            bottom_half = self.cards[26:]
        if in_faro:
            # TODO: is this the simplest way to switch variables for one another?
            top_half, bottom_half = bottom_half, top_half
        self.cards = list(itertools.chain(*zip(top_half, bottom_half)))
        return self

    # TODO: faro a smaller packet inside a bigger one
    # def straddle_faro(self, other: 'Deck' = None) -> 'Deck':
    #     pass

    def cut_cards(self, number: int) -> 'Deck':
        cut = self.cards[:number]
        self.cards = self.cards[number:]

        return Deck(cut)

    def cull_card(self, card: 'Card', index: int) -> 'Deck':
        card_index = self.cards.index(card)
        card = self.cards.pop(card_index)
        self.cards.insert(index, card)
        return self

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
        first, second = random.sample([self, deck], 2)
        # TODO: test with random.randint = 1; riffle_shuffle == faro_shuffle
        while not (first.is_empty() and second.is_empty()):
            random_value = random.randint(1, 5)
            assembled += first.cards[:random_value]
            first.cards = first.cards[random_value:]

            random_value = random.randint(1, 5)
            assembled += second.cards[:random_value]
            second.cards = second.cards[random_value:]

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

    def find_flushes(self, minimum_amount: int = 2) -> List[FlushFound]:
        flushes = []

        candidate_index = 0
        candidate = [self.cards[0]]
        for i, card in enumerate(self.cards[1:]):
            if card.has_same_suit(candidate[0]):
                candidate.append(card)
            else:
                if len(candidate) >= minimum_amount:
                    flushes.append(FlushFound(candidate_index, candidate))

                # i is relative to self.cards[1:] but we want the representation from self.cards
                candidate_index = i + 1
                candidate = [card]

        if len(candidate) >= minimum_amount:
            flushes.append(FlushFound(candidate_index, candidate))

        return flushes

    def find_straights(self, minium_amount: int = 2) -> List[StraightFound]:
        straights = []
        candidate_index = 0
        candidate = [self.cards[0]]

        return straights

    def is_a_flush(self) -> bool:
        suit = self.cards[0].suit
        return all(card.suit == suit for card in self.cards)

    def copy(self) -> 'Deck':
        return Deck(self.cards.copy())

    def __eq__(self, other: 'Deck') -> bool:
        if not isinstance(other, Deck):
            return False

        return other.cards == self.cards

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
