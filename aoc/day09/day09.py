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
        self.calculate_zero_differences()

    def parse_input(self) -> None:
        for line in [x.split() for x in self.input.splitlines()]:
            self.readings.append([[int(num) for num in line]])

    def find_differences(self, numlist: List[int]) -> List[int]:
        result = []
        for i in range(1, len(numlist)):
            result.append(numlist[i] - numlist[i - 1])
        return result

    def calculate_zero_differences(self) -> None:
        for reading in self.readings:
            diff = self.find_differences(reading[0])
            while any(diff):
                reading.append(diff)
                diff = self.find_differences(diff)

    def find_back_history(self, reading: List[List[int]]) -> int:
        result = 0
        for row in reversed(reading):
            result += row[-1]
        return result

    def find_front_history(self, reading: List[List[int]]) -> int:
        result = 0
        for row in reversed(reading):
            result = row[0] - result
        return result

    def part_one(self) -> int:
        result = 0
        for reading in self.readings:
            result += self.find_back_history(reading)
        return result

    def part_two(self) -> int:
        result = 0
        for reading in self.readings:
            result += self.find_front_history(reading)
        return result
