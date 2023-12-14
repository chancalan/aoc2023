# You can copy/paste this template to start a new day

"""08: Haunted Wasteland"""
import aoc.util
from math import lcm


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.instructions = ""
        self.map = {}
        self.starts = []
        self.parse_input()

    def parse_input(self) -> None:
        self.input = self.input.splitlines()
        self.instructions = self.input[0]
        for line in self.input[2:]:
            key, value = line.split(" = ")
            if key[2] == "A":
                self.starts.append(key)
            self.map[key] = (value[1:4], value[6:9])

    def part_one(self) -> int:
        step = 0
        isize = len(self.instructions)
        cur = "AAA"
        while cur != "ZZZ":
            dir = self.instructions[step % isize]
            if dir == "R":
                cur = self.map[cur][1]
            else:
                cur = self.map[cur][0]
            step += 1
        return step

    def part_two(self) -> int:
        """
        did some investigation and found out that each path's cycle are the same
        meaning from steps from start -> end and end -> end are the same
        so we just need to find the least common multiple (LCM) for each cycle
        """
        isize = len(self.instructions)
        steps = []
        for start in self.starts:
            step = 0
            cur = start
            # while reach_end == 0 and cur not in seen:
            while cur[2] != "Z":
                dir = self.instructions[step % isize]
                if dir == "R":
                    cur = self.map[cur][1]
                else:
                    cur = self.map[cur][0]
                step += 1
            steps.append(step)
        return lcm(*steps)
