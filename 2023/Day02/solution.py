from sys import argv


class Reveal:
    def __init__(self) -> None:
        self.Red: int = 0
        self.Green: int = 0
        self.Blue: int = 0

    def __str__(self):
        return "Red: {:02}, Green: {:02}, Blue: {:02}".format(
            self.Red, self.Green, self.Blue
        )


class Game:
    def __init__(self) -> None:
        self.num: int
        self.reveals: list[Reveal] = list()
        pass

    def __str__(self):
        return "Game {:02}: {}".format(self.num, [r.__str__() for r in self.reveals])


LIMITS = {"Red": 12, "Green": 13, "Blue": 14}


class Solution:
    games: list[Game] = list()

    def getInput(this, file: str):
        list = []
        with open(file) as fp:
            for line in fp:
                line = line.strip()
                split1 = line.split(":")
                if len(split1) <= 1:
                    continue

                gameNum = int(split1[0].split(" ")[1])
                game = Game()

                game.num = gameNum

                revealsStrs = split1[1].split(";")

                for revealStr in revealsStrs:
                    reveal = Reveal()
                    colors = revealStr.split(",")
                    for color in colors:
                        components = color.split(" ")
                        value = int(components[1])

                        match components[2]:
                            case "red":
                                reveal.Red += value
                            case "green":
                                reveal.Green += value
                            case "blue":
                                reveal.Blue += value

                    game.reveals.append(reveal)

                this.games.append(game)

    def solve1(this) -> int:
        def gameIsPossible(game: Game) -> bool:
            def isPossibleReveal(r: Reveal) -> bool:
                return (
                    r.Red <= LIMITS["Red"]
                    and r.Green <= LIMITS["Green"]
                    and r.Blue <= LIMITS["Blue"]
                )

            return all([isPossibleReveal(r) for r in game.reveals])

        possibleGames = [game for game in this.games if gameIsPossible(game)]

        for game in possibleGames:
            print(game)

        return sum([game.num for game in possibleGames])

    def solve2(this) -> int:
        def getPower(game: Game) -> int:
            maxRed = max([r.Red for r in game.reveals])
            maxGreen = max([r.Green for r in game.reveals])
            maxBlue = max([r.Blue for r in game.reveals])
            return maxRed * maxGreen * maxBlue

        return sum([getPower(game) for game in this.games])


if __name__ == "__main__":
    file = "input.txt"
    if argv.__len__() > 1:
        file = argv[1]

    solver = Solution()
    solver.getInput(file)
    print("Solution 1: {}".format(solver.solve1()))
    print("Solution 2: {}".format(solver.solve2()))
