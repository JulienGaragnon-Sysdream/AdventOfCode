from sys import argv
import numpy as np


class Solution:
    lines: list = list()

    def getInput(this, file: str):
        list = []
        with open(file) as fp:
            for line in fp:
                this.lines.append(line)

    def solve1(this) -> int:
        sum = 0
        for line in this.lines:
            digits = list(filter(lambda s:  s.isdigit(), line))
            if (len(digits)) > 0:
                value = digits[0] + digits[-1]
                sum += int(value)

        return sum

    numbers = {
        "one": 1,
        "two" :2,
        "three" :3,
        "four" :4,
        "five" :5,
        "six" :6,
        "seven" :7,
        "eight" :8,
        "nine" :9
    }

    def solve2(this) -> int:
        sum = 0
        for line in this.lines:
            line_nums = list()
            for i in range(len(line)):
                if line[i].isdigit() :
                    line_nums.append(int(line[i]))
                    continue

                for number in this.numbers :
                    if line[i:].startswith(number):
                        line_nums.append(this.numbers[number])
                        break

            sum += line_nums[0] * 10 + line_nums[-1]
        return sum




if __name__ == "__main__":
    file = "input.txt"
    if argv.__len__() > 1:
        file = argv[1]

    solver = Solution()
    solver.getInput(file)
    print("Solution 1: {}".format(solver.solve1()))
    print("Solution 2: {}".format(solver.solve2()))
