from typing import Tuple, List
from mnemonica.deck.card import Card


class PairFound:
    def __init__(self, pos: int, found: Tuple[Card, Card]) -> None:
        self.pos = pos
        self.found = found

    def __repr__(self) -> str:
        return f"[Pair found] At pos [{self.pos + 1}], {self.found[0]}, {self.found[1]}"


class ThreeOfAKindFound:
    def __init__(self, pos: int, found: Tuple[Card, Card, Card]) -> None:
        self.pos = pos
        self.found = found

    def __repr__(self) -> str:
        return f"[Three of a kind found] At pos [{self.pos + 1}], {self.found[0]}, {self.found[1]}, {self.found[2]}"


class FourOfAKindFound:
    def __init__(self, pos: int, found: Tuple[Card, Card, Card, Card]) -> None:
        self.pos = pos
        self.found = found

    def __repr__(self) -> str:
        return (f"[Four of a kind found] At pos [{self.pos + 1}], "
                f"{self.found[0]}, "
                f"{self.found[1]}, "
                f"{self.found[2]}, "
                f"{self.found[3]}")


class FlushFound:
    def __init__(self, pos: int, found: List[Card]) -> None:
        self.pos = pos
        self.found = found

    def __repr__(self) -> str:
        return f"[Flush found] At pos [{self.pos + 1}], {self.found}"

class StraightFound:
    def __init__(self, pos: int, found: List[Card]) -> None:
        self.pos = pos
        self.found = found

    def __repr__(self) -> str:
        return f"[Straight found] At pos [{self.pos + 1}], {self.found}"
