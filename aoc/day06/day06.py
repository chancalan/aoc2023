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
            count = 0
            prev = 0
            half = -(-time // 2)
            for i in range(1, half + 1):
                gone = i * (time - i)
                if gone == prev:
                    count *= 2
                    break
                if gone > distance:
                    prev = gone
                    count += 1
            else:
                count = (count * 2) - 1
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
