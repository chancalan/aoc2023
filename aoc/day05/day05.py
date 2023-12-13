# You can copy/paste this template to start a new day

"""05: If You Give A Seed A Fertilizer"""
import aoc.util


# all solutions should subclass the `Solver` exposed by `aoc.util`
# this class MUST be called Solver for the CLI discovery to work
class Solver(aoc.util.Solver):
    def __init__(self, input: str):
        # sets self.input to the provided input
        super(Solver, self).__init__(input)
        self.section_to_i = {
            "seed-to-soil": 0,
            "soil-to-fertilizer": 1,
            "fertilizer-to-water": 2,
            "water-to-light": 3,
            "light-to-temperature": 4,
            "temperature-to-humidity": 5,
            "humidity-to-location": 6,
        }
        self.seeds = []
        self.maps = [[] for _ in range(7)]
        self.parse_input()

    def parse_input(self) -> None:
        self.input = self.input.splitlines()
        index = 0
        section = []
        for line in self.input:
            if len(line) == 0:
                continue
            items = line.split()
            if items[0] == "seeds:":
                self.seeds = [int(i) for i in items[1:]]
            elif items[0] in self.section_to_i:
                self.maps[index] = section
                index = self.section_to_i[items[0]]
                section = []
            else:  # mapping reading
                section.append(
                    ((int(items[1]), int(items[1]) + int(items[2])), (int(items[0]), int(items[0]) + int(items[2])))
                )
        self.maps[index] = section

    def part_one(self) -> int:
        result = []
        # each seed
        for num in self.seeds:
            # each section of map
            for section in self.maps:
                # each line item in each section of map
                for item in section:
                    if item[0][0] <= num < item[0][1]:
                        num = item[1][0] + (num - item[0][0])
                        break
            result.append(num)
        return min(result)

    def part_two(self) -> int:
        seeds = []
        for i in range(0, len(self.seeds), 2):
            seeds.append((self.seeds[i], self.seeds[i] + self.seeds[i + 1]))
        for section in self.maps:
            temp = []
            while len(seeds) > 0:
                seed = seeds.pop()
                for item in section:
                    temp_start = max(item[0][0], seed[0])
                    temp_end = min(item[0][1], seed[1])
                    if temp_start < temp_end:
                        temp.append((temp_start - item[0][0] + item[1][0], temp_end - item[0][0] + item[1][0]))
                        if temp_start > seed[0]:
                            seeds.append((seed[0], temp_start))
                        if temp_end < seed[1]:
                            seeds.append((temp_end, seed[1]))
                        break
                else:
                    temp.append(seed)
            seeds = temp
        return min(seeds)[0]
