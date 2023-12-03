# You can copy/paste this template to start a new day

"""03: Gear Ratios"""
import aoc.util
import re
from typing import List


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.sym_pos = set()
        self.num_pos = {}
        self.parse_data()

    def get_possible_symbol(self) -> List[str]:
        # assuming self.input has been splitlines()
        symbols = set()
        for line in self.input:
            for i in ['0','1','2','3','4','5','6','7','8','9','.']:
                line = line.replace(i,'')
            for item in line:
                symbols.add(item)
        return list[symbols]

    def parse_data(self) -> None:
        self.input = self.input.splitlines()
        symbols = ['#', '=', '/', '-', '%', '@', '*', '&', '$', '+']
        for r, line in enumerate(self.input):
            c = 0
            while c < len(self.input[r]):
                if line[c] == '.':
                    c += 1
                    continue
                elif line[c] in symbols:
                    self.sym_pos.add((r, c))
                    c += 1
                else:  # it's a number
                    temp = [line[c]]
                    temp2 = {(r, c)}
                    c += 1
                    while c < len(self.input[r]) and line[c].isdigit():
                        temp.append(line[c])
                        temp2.add((r, c))
                        c += 1
                    num = int(''.join(temp))
                    for item in temp2:
                        self.num_pos[item] = {
                            'num': num,
                            'neighbor': temp2
                        }

    def part_one(self) -> int:
        result = 0
        for symr, symc in self.sym_pos:
            found = set()
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                new_pos = (symr + dr, symc + dc)
                if new_pos in found:
                    continue
                elif new_pos in self.num_pos:
                    result += self.num_pos[new_pos]['num']
                    found = found | self.num_pos[new_pos]['neighbor']
        return result

    def part_two(self) -> int:
        # TODO: actually return the answer
        return 0
