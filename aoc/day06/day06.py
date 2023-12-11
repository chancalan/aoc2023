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
        time = self.input[0].split()[1:]
        distance = self.input[1].split()[1:]
        for i in range(len(time)):
            self.rounds.append((time[i], distance[i]))

    def solution(self, rounds) -> int:
        result = 1
        for time, distance in rounds:
            # binary search to find the first millisecond that will beat the record
            low = 0
            high = half = time // 2
            while low <= high:
                mid = (high + low) // 2
                if mid * (time - mid) > distance:
                    high = mid - 1
                else:
                    low = mid + 1

            # using some math to calculate the count
            if half == (time - half):
                count = ((half - low + 1) * 2) - 1
            else:
                count = (half - low + 1) * 2
            result *= count
        return result

    def part_one(self) -> int:
        rounds = []
        for t, d in self.rounds:
            rounds.append((int(t), int(d)))
        return self.solution(rounds)

    def part_two(self) -> int:
        time = []
        distance = []
        for t, d in self.rounds:
            time.append(t)
            distance.append(d)
        return self.solution([(int("".join(time)), int("".join(distance)))])
