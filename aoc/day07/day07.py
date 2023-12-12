# You can copy/paste this template to start a new day

"""07: Camel Cards"""
import aoc.util
from collections import Counter
from typing import List


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.hands = {}
        self.parse_input()

    def parse_input(self) -> int:
        """
        Storing the bid
        Storing the counter of all the characters
        Storing the counter of the counter of characters
        """
        self.input = self.input.splitlines()
        for line in self.input:
            hand, bid = line.split()
            char_counter = Counter(hand)
            self.hands[hand] = {
                "bid": int(bid),
                "char_counter": char_counter,
                "counter": Counter(char_counter.values()),
            }

    def hand_ranking(self, hand: str, counter) -> int:
        """
        Given the counter of the counter of characters
        Return the ranking where
        - 6: five of a kind
        - 5: four of a kind
        - 4: full house
        - 3: three of a kind
        - 2: two pairs
        - 1: one pair
        - 0: high card, no character matching
        """
        rank = 0
        if 5 in counter:
            rank = 6
        elif 4 in counter:
            rank = 5
        elif 3 in counter:
            if 2 in counter:
                rank = 4
            else:
                rank = 3
        elif 2 in counter:
            if counter[2] == 2:
                rank = 2
            else:
                rank = 1
        # for the else, i would have been 0
        return rank

    def card_ranking(self, strength_rule: str, ranks: List[List[str]]) -> int:
        """
        Given the card strength rule from weak to strong and the rankings of the hands
        Return the bidding result
        """
        result = 0
        rank = 1
        for tier in ranks:
            for hand in sorted(tier, key=lambda temp: [strength_rule.index(c) for c in temp]):
                temp = self.hands[hand]["bid"] * rank
                result += temp
                rank += 1
        return result

    def part_one(self) -> int:
        ranks = [[] for _ in range(7)]
        for hand in self.hands:
            rank = self.hand_ranking(hand, self.hands[hand]["counter"])
            ranks[rank].append(hand)
        return self.card_ranking("23456789TJQKA", ranks)

    def part_two(self) -> int:
        ranks = [[] for _ in range(7)]
        for hand in self.hands:
            # deleting the counter for 'J'
            del self.hands[hand]["char_counter"]["J"]
            if len(self.hands[hand]["char_counter"]) == 0:
                # no counter at all, meaning the original hand is all 'J's
                # five of a kind = 6
                ranks[6].append(hand)
                continue
            # replace J with the most common characters to create the highest ranking hand possible
            replacement = hand.replace("J", self.hands[hand]["char_counter"].most_common()[0][0])
            char_counter = Counter(replacement)
            counter = Counter(char_counter.values())
            ranks[self.hand_ranking(replacement, counter)].append(hand)
        return self.card_ranking("J23456789TQKA", ranks)
