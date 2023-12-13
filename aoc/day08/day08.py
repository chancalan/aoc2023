# You can copy/paste this template to start a new day

"""08: Haunted Wasteland"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.instructions = ''
        self.map = {}
        self.parse_input()

    def parse_input(self) -> None:
        self.input = self.input.splitlines()
        self.instructions = self.input[0]
        for line in self.input[2:]:
            key, value = line.split(' = ')
            self.map[key] = (value[1:4], value[6:9])

    def part_one(self) -> int:
        step = 0
        isize = len(self.instructions)
        cur = 'AAA'
        while cur != 'ZZZ':
            dir = self.instructions[step % isize]
            if dir == 'R':
                cur = self.map[cur][1]
            else:
                cur = self.map[cur][0]
            step += 1
        return step

    def part_two(self) -> int:
        # TODO: actually return the answer
        return 0
