from sys import argv


class Widget:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol
        self.numbers = list[int]()

    def __str__(self):
        return "{}: {}".format(self.symbol, self.numbers)


def getNumber(line: str, start: int):
    end = start
    while start >= 0 and line[start].isdigit():
        start -= 1
    start += 1

    while end < len(line) and line[end].isdigit():
        end += 1
    end -= 1

    number = line[start : end + 1]
    # print("Found number {} from {} to {} in {}".format(number, start, end, line))
    num = int(number)
    return (num, start, end)


class Solution:
    def __init__(self) -> None:
        self.widgets = list[Widget]()

    def getInput(self, file: str):
        with open(file) as fp:
            lines = fp.read().splitlines()

            for line_num, line in enumerate(lines):
                for char_num, char in enumerate(line):
                    if not char.isdigit() and char != ".":
                        print(
                            "Found symbol {}  at {}:{}".format(char, line_num, char_num)
                        )
                        widget = Widget(char)
                        self.widgets.append(widget)
                        for i, j in [
                            (-1, -1),
                            (-1, 0),
                            (-1, +1),
                            (0, -1),
                            (0, +1),
                            (+1, -1),
                            (+1, 0),
                            (+1, +1),
                        ]:
                            if (
                                line_num + i < 0
                                or line_num + i >= len(lines)
                                or char_num + j < 0
                                or char_num + j >= len(line)
                            ):
                                continue

                            if lines[line_num + i][char_num + j].isdigit():
                                num, _, _ = getNumber(
                                    lines[line_num + i], char_num + j
                                )
                                if num not in widget.numbers:
                                    widget.numbers.append(num)
        print(*self.widgets)

    def solve1(self) -> int:
        return sum(sum(w.numbers) for w in self.widgets)

    def solve2(self) -> int:
        gears = [w for w in self.widgets if w.symbol == "*" and len(w.numbers) == 2]
        return sum(w.numbers[0] * w.numbers[1] for w in gears)


if __name__ == "__main__":
    file = "input.txt"
    if argv.__len__() > 1:
        file = argv[1]

    solver = Solution()
    solver.getInput(file)
    print("Solution 1: {}".format(solver.solve1()))
    print("Solution 2: {}".format(solver.solve2()))
