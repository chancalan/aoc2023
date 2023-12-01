"""01: Trebuchet?!"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.input = self.input.splitlines()

    def find_num(self, line: str) -> int:
        """
        Input: line of string
        Output: an int formed by the first digit and last digit
        int(first_last)
        """
        for c in line:
            if c.isdigit():
                num = [c]
                break
        for c in line[::-1]:
            if c.isdigit():
                num.append(c)
                break
        return int(''.join(num))

    def part_one(self) -> int:
        result = 0
        for line in self.input:
            result += self.find_num(line)
        return result

    def part_two(self) -> int:
        """
        possible mix up, first 4 for forward, last 4 for backward
        - nineight
        - eightwo
        - eightree
        - twone
        - oneight
        - threeight
        - fivenight
        - sevenine
        """
        replacement = {
            'one': 'o1e',
            'two': 't2o',
            'three': 't3e',
            'four': '4',
            'five': 'f5e',
            'six': '6',
            'seven': 's7n',
            'eight': 'e8t',
            'nine': 'n9e'
        }
        result = 0
        for line in self.input:
            for key in replacement:
                line = line.replace(key, replacement[key])
            result += self.find_num(line)
        return result
