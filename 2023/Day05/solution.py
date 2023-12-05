from sys import argv


class AlmanacRange:
    def __init__(self, source: int, destination: int, length: int) -> None:
        self.source = source
        self.destination = destination
        self.length = length
        self.end = source + length

    def map(self, number: int) -> int:
        return number - self.source + self.destination

    def contains(self, number: int) -> bool:
        return number >= self.source and number < self.end

    def __str__(self):
        return "  {}, {}->{} {}".format(
            self.source, self.end, self.destination, self.length
        )


class AlmanacMap:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ranges = list[AlmanacRange]()

    def __str__(self):
        return "  {}\n   Ranges: {}".format(self.name, *self.ranges)

    def map(self, number: int) -> int:
        inRange = [r for r in self.ranges if r.contains(number)]

        if len(inRange) == 0:
            return number
        return inRange[0].map(number)


class myRange:
    def __init__(self, start, stop) -> None:
        self.start = start
        self.stop = stop
        pass

    def __str__(self):
        return "myrange({}, {})".format(self.start, self.stop)


class Solution:
    def __init__(self) -> None:
        self.almanacs = list[AlmanacMap]()
        self.seed = list[int]()

    def getInput(self, file: str):
        with open(file) as fp:
            for line in fp:
                line = line.strip()

                if line == "":
                    continue

                if line.startswith("seeds:"):
                    self.seeds = [int(x) for x in line.split(":")[1].split()]
                    continue

                if line.endswith("map:"):
                    almanac = AlmanacMap(line.split(" ")[0])
                    self.almanacs.append(almanac)
                    continue

                nums = [int(x) for x in line.split()]
                self.almanacs[-1].ranges.append(AlmanacRange(nums[1], nums[0], nums[2]))

    def solve1(self) -> int:
        numbers = list(self.seeds)

        for almanac in self.almanacs:
            numbers = [almanac.map(x) for x in numbers]

        return min(numbers)

    def solve2(self) -> int:
        numbers = list[myRange]()

        for i in range(0, len(self.seeds), 2):
            numbers.append(myRange(self.seeds[i], self.seeds[i] + self.seeds[i + 1]))

        for almanac in self.almanacs:
            print("handling almanac {}".format(almanac.name))
            newNumbers = list[myRange]()
            for seeds in numbers:
                newstart = almanac.map(seeds.start)
                newend = almanac.map(seeds.stop)

                # print(
                #     "mapped {}, {} -> {}, {}".format(
                #         seeds.start, seeds.stop, newstart, newend
                #     )
                # )

                for r in almanac.ranges:
                    if r.source >= seeds.start and r.source <= seeds.stop:
                        newrange = myRange(newstart, almanac.map(r.source-1))
                        # print("Splitting new {}".format(newrange))
                        newNumbers.append(newrange)
                        newstart = almanac.map(seeds.start + 1)
                    if r.end >= seeds.start and r.end <= seeds.stop:
                        newrange = myRange(almanac.map(r.end), newend)
                        # print("Splitting new {}".format(newrange))
                        newNumbers.append(newrange)
                        newend = almanac.map(r.end-1)

                # print("Adding {}".format(myRange(newstart, newend)))
                newNumbers.append(myRange(newstart, newend))

            numbers = newNumbers

        return min([k.start for k in numbers])

    def __str__(self):
        return "Seeds: {}\n  Almanacs:\n{}".format(self.seeds, "\n".join(self.almanacs))


if __name__ == "__main__":
    file = "input.txt"
    if argv.__len__() > 1:
        file = argv[1]

    solver = Solution()
    solver.getInput(file)
    print("Solution 1: {}".format(solver.solve1()))
    print("Solution 2: {}".format(solver.solve2()))
