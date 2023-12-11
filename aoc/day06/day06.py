# You can copy/paste this template to start a new day

"""06: Wait For It"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.rounds = []
        self.parse_input()

    def parse_input(self) -> None:
        self.input = self.input.splitlines()
        time = [int(i) for i in self.input[0].split()[1:]]
        distance = [int(i) for i in self.input[1].split()[1:]]
        for i in range(len(time)):
            self.rounds.append((time[i], distance[i]))

    def part_one(self) -> int:
        result = 1
        for time, distance in self.rounds:
            count = 0
            half = -(-time // 2)
            for i in range(1, time + 1):
                if i * (time - i) > distance:
                    count += 1
            result *= count
        return result

    def part_two(self) -> int:
        # TODO: actually return the answer
        return 0
