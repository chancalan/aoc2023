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

    def parse_input(self) -> None:
        self.input = self.input.splitlines()
        for line in self.input:
            _, sets = line.split(': ')
            game = []
            match = re.findall(r'(\d+) (\w+),? ?(; )?', sets)
            temp_set = {}
            for item in match:
                temp_set[item[1]] = int(item[0])
                if len(item[2]) != 0:
                    game.append(temp_set)
                    temp_set = {}
            game.append(temp_set)
            self.games.append(game)

    def part_one(self) -> int:
        target = {
            'red': 12,
            'green': 13,
            'blue': 14
        }
        result = 0
        for i, game in enumerate(self.games):
            possible = True
            for cubes in game:
                for color in cubes:
                    if cubes[color] > target[color]:
                        possible = False
                        break
                if not possible:
                    break
            else:
                result += i + 1
        return result

    def part_two(self) -> int:
        result = 0
        atleast = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for game in self.games:
            atleast['red'] = 0
            atleast['green'] = 0
            atleast['blue'] = 0
            for cubes in game:
                for color in cubes:
                    atleast[color] = max(atleast[color], cubes[color])
            temp = 1
            for color in atleast:
                temp *= atleast[color]
            result += temp

        return result
