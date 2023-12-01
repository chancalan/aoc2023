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
        for c in line:
            if c.isdigit():
                num = int(c) * 10
                break
        for c in line[::-1]:
            if c.isdigit():
                num += int(c)
                break
        return num

    def part_one(self) -> int:
        result = 0
        for line in self.input:
            result += self.find_num(line)
        return result

    def part_two(self) -> int:
        forward_order = [
            "nineight",
            "eightwo",
            "eighthree",
            "twone",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        backward_order = [
            "oneight",
            "threeight",
            "fiveight",
            "sevenine",
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]
        replacement = {
            "nineight": "9ight",
            "eightwo": "8wo",
            "eighthree": "8hree",
            "twone": "2ne",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "oneight": "on8",
            "threeight": "thre8",
            "fiveight": "fiv8",
            "sevenine": "seve9",
        }
        result = 0
        for line in self.input:
            forward = line
            for key in forward_order:
                forward = forward.replace(key, replacement[key])
            for c in forward:
                if c.isdigit():
                    num = int(c) * 10
                    break
            backward = line
            for key in backward_order:
                backward = backward.replace(key, replacement[key])
            for c in backward[::-1]:
                if c.isdigit():
                    num += int(c)
                    break
            result += num
        return result
