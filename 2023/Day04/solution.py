from sys import argv


class Card:
    def __init__(self, number: int) -> None:
        self.number = number
        self.winning = list[int]()
        self.revealed = list[int]()

    def wins(self) -> list[int]:
        return [x for x in self.revealed if x in self.winning]

    def __str__(self):
        return "Card {}: {} | ".format(self.number, *self.winning, *self.revealed)


class Solution:
    def __init__(self) -> None:
        self.cards = list[Card]()

    def getInput(self, file: str):
        with open(file) as fp:
            lines = fp.read().splitlines()

            for line in lines:
                split1 = line.split(":")
                if len(split1) <= 1:
                    continue

                card_num = int(split1[0].split()[1])
                card = Card(card_num)
                self.cards.append(card)

                lists = split1[1].split("|")

                card.winning = [int(n) for n in lists[0].split()]
                card.revealed = [int(n) for n in lists[1].split()]

    def solve1(self) -> int:
        sum = 0
        for card in self.cards:
            wins = card.wins()
            if len(wins) > 0:
                sum += 2 ** (len(wins) - 1)
        return sum

    def solve2(self) -> int:
        mult = [1 for _ in self.cards]

        for card in self.cards:
            wins = len(card.wins())

            for x in range(card.number, card.number + wins):
                mult[x] += mult[card.number - 1]

        return sum(mult)


if __name__ == "__main__":
    file = "input.txt"
    if argv.__len__() > 1:
        file = argv[1]

    solver = Solution()
    solver.getInput(file)
    print("Solution 1: {}".format(solver.solve1()))
    print("Solution 2: {}".format(solver.solve2()))
