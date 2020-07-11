from dataclasses import dataclass, field
from typing import List, Tuple

bites: List[int] = [283, 282, 281, 263, 255, 230, 216, 204, 197, 196, 195]
names: List[str] = [
    "snow",
    "natalia",
    "alex",
    "maquina",
    "maria",
    "tim",
    "kenneth",
    "fred",
    "james",
    "sara",
    "sam",
]


@dataclass
class Ninja:
    """
    The Ninja class will have the following features:

    string: name
    integer: bites
    support <, >, and ==, based on bites
    print out in the following format: [469] bob
    """
    name: str
    bites: int

    def __str__(self):
        return f"[{self.bites}] {self.name}"

    def __lt__(self, other):
        return self.bites < other.bites

    def __gt__(self, other):
        return self.bites > other.bites

    def __eq__(self, other):
        return self.bites == other.bites


@dataclass
class Rankings:
    """
    The Rankings class will have the following features:

    method: add() that adds a Ninja object to the rankings
    method: dump() that removes/dumps the lowest ranking Ninja from Rankings
    method: highest() returns the highest ranking Ninja, but it takes an optional
            count parameter indicating how many of the highest ranking Ninjas to return
    method: lowest(), the same as highest but returns the lowest ranking Ninjas, also
            supports an optional count parameter
    returns how many Ninjas are in Rankings when len() is called on it
    method: pair_up(), pairs up study partners, takes an optional count
            parameter indicating how many Ninjas to pair up
    returns List containing tuples of the paired up Ninja objects
    """
    rankings: List[Ninja] = field(default_factory=list)

    def __len__(self):
        return len(self.rankings)

    def add(self, ninja: Ninja):
        self.rankings.append(ninja)

    def dump(self):
        lowest_ranked = min(self.rankings)
        self.rankings.remove(lowest_ranked)
        return lowest_ranked

    def _sorted(self, reverse=False, count=1):
        return sorted(self.rankings, reverse=reverse)[:count]

    def highest(self, count=1):
        return self._sorted(reverse=True, count=count)

    def lowest(self, count=1):
        return self._sorted(count=count)

    def pair_up(self, count=3):
        highest_ranking_ninjas = self.highest(count=count)
        lowest_ranking_ninjas = self.lowest(count=count)

        return list(zip(highest_ranking_ninjas, lowest_ranking_ninjas))
