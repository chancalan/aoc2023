# You can copy/paste this template to start a new day

"""02: Cube Conundrum"""
import aoc.util
import re


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.games = []
        self.parse_input()
        self.part1 = 0
        self.part2 = 0
        self.solution()

    def parse_input(self) -> None:
        self.input = self.input.splitlines()
        for line in self.input:
            _, sets = line.split(": ")
            game = []
            match = re.findall(r"(\d+) (\w+),? ?(; )?", sets)
            temp_set = {}
            for item in match:
                temp_set[item[1]] = int(item[0])
                if len(item[2]) != 0:
                    game.append(temp_set)
                    temp_set = {}
            game.append(temp_set)
            self.games.append(game)

    def solution(self) -> None:
        # used for part 1
        target = {"red": 12, "green": 13, "blue": 14}
        for i, game in enumerate(self.games):
            # used for part 2
            atleast = {"red": 0, "green": 0, "blue": 0}
            possible = True  # used for part 1

            for cubes in game:
                for color in cubes:
                    atleast[color] = max(atleast[color], cubes[color])
                    if cubes[color] > target[color]:
                        possible = False
            if possible:
                self.part1 += i + 1
            temp = 1
            for color in atleast:
                temp *= atleast[color]
            self.part2 += temp

    def part_one(self) -> int:
        return self.part1

    def part_two(self) -> int:
        return self.part2
