# You can copy/paste this template to start a new day

"""04: Scratchcards"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.cards = []
        self.parse_input()
        self.num_wins = [0] * len(self.cards)

    def parse_input(self) -> None:
        self.input = self.input.splitlines()
        for line in self.input:
            _, nums = line.split(": ")
            wins, nums = nums.split(" | ")
            wins = list(filter(None, wins.split(" ")))
            nums = set(filter(None, nums.split(" ")))
            self.cards.append([wins, nums])

    def part_one(self) -> int:
        points = 0
        for i, (wins, nums) in enumerate(self.cards):
            m = []
            for win in wins:
                if win in nums:
                    m.append(win)
            self.num_wins[i] = len(m)
            if len(m) == 1:
                points += 1
            elif len(m) > 1:
                temp = 1
                for _ in range(len(m) - 1):
                    temp *= 2
                points += temp
        return points

    def part_two(self) -> int:
        num_cards = [1] * len(self.cards)
        for i, num in enumerate(self.num_wins):
            original = num_cards[i]
            for card in range(i + 1, i + 1 + num):
                num_cards[card] += original
        return sum(num_cards)
