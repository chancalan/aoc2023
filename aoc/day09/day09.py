# You can copy/paste this template to start a new day

"""09: Mirage Maintenance"""
import aoc.util
from typing import List


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.readings = []
        self.parse_input()

    def parse_input(self) -> None:
        for line in [x.split() for x in self.input.splitlines()]:
            self.readings.append([int(num) for num in line])

    def find_differences(self, numlist: List[int]) -> List[int]:
        result = []
        for i in range(1, len(numlist)):
            result.append(numlist[i] - numlist[i - 1])
        return result

    def find_history(self, reading: List[int]) -> int:
        calculations = [reading]
        diff = self.find_differences(reading)
        while any(diff):
            calculations.append(diff)
            diff = self.find_differences(diff)

        result = 0
        for row in reversed(calculations):
            result += row[-1]
        return result

    def part_one(self) -> int:
        result = 0
        for reading in self.readings:
            result += self.find_history(reading)
        return result

    def part_two(self) -> int:
        # TODO: actually return the answer
        return 0
