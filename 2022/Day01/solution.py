from sys import argv
import numpy as np

class Solution:
    sums : np.array

    def getInput(this, file: str):
        list = []
        with open(file) as fp:
            current = 0
            for line in fp:
                line = line.removesuffix("\n")
                if (line == "") :
                    list.append(current)
                    current = 0
                else :
                    lineInt = int(line)
                    current += lineInt
        this.sums = np.array(list)

    def solve1(this) -> int:
        return max(this.sums)


    def solve2(this) -> int:
        return np.sort(this.sums)[-3:].sum()



if __name__ == '__main__':

    file = "input.txt"
    if (argv.__len__() > 1):
        file = argv[1]


    solver = Solution()
    solver.getInput(file)
    print(solver.solve1())
    print(solver.solve2())
