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
        self.input = self.input.splitlines()
        for line in self.input:
            hand, bid = line.split()
            self.hands[hand] = int(bid)

    def part1_hand_ranking(self) -> List[List[str]]:
        ranks = [[] for _ in range(7)]
        for hand in self.hands:
            char_counter = Counter(hand)
            counter = Counter(char_counter.values())
            i = 0
            if 5 in counter:
                i = 6
            elif 4 in counter:
                i = 5
            elif 3 in counter:
                if 2 in counter:
                    i = 4
                else:
                    i = 3
            elif 2 in counter:
                if counter[2] == 2:
                    i = 2
                else:
                    i = 1
            # for the else, i would have been 0
            ranks[i].append(hand)
        return ranks

    def part2_hand_ranking(self) -> List[List[str]]:
        ranks = [[] for _ in range(7)]
        for hand in self.hands:
            pass
        return ranks

    def card_ranking(self, strength_rule: str, ranks: List[List[str]]) -> int:
        result = 0
        rank = 1
        for tier in ranks:
            for hand in sorted(tier, key=lambda temp: [strength_rule.index(c) for c in temp]):
                temp = (self.hands[hand] * rank)
                result += temp
                rank += 1
        return result

    def part_one(self) -> int:
        ranks = self.part1_hand_ranking()
        return self.card_ranking('23456789TJQKA', ranks)

    def part_two(self) -> int:
        ranks = self.part2_hand_ranking()
        return self.card_ranking('J23456789TQKA', ranks)
