matrix = []
visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]

def parseInput():
    with open("inputTest.txt") as file:
        lines = file.readlines()
        for line in lines:
            row = list(line.strip())
            matrix.append(row)


def findGuardPath():
    position = (0, 0)
    direction = "^"

    numbersOfSteps = 0

    def findInitialPosition():
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == "^":
                    return (r, c)

    position = findInitialPosition()

    while True:
        if not visited[position[0]][position[1]]:
                visited[position[0]][position[1]] = True
                numbersOfSteps += 1

        if direction == "^":
            if (position[0] - 1 < 0):
                break
            if matrix[position[0] - 1][position[1]] == "#":
                direction = ">"
                position = (position[0], position[1] + 1)
            else:
                position = (position[0] - 1, position[1])
        elif direction == ">":
            if (position[1] + 1 >= len(matrix[0])):
                break
            if matrix[position[0]][position[1] + 1] == "#":
                direction = "v"
                position = (position[0] + 1, position[1])
            else:
                position = (position[0], position[1] + 1)
        elif direction == "v":
            if (position[0] + 1 >= len(matrix)):
                break
            if matrix[position[0] + 1][position[1]] == "#":
                direction = "<"
                position = (position[0], position[1] - 1)
            else:
                position = (position[0] + 1, position[1])
        elif direction == "<":
            if (position[1] - 1 < 0):
                break
            if matrix[position[0]][position[1] - 1] == "#":
                direction = "^"
                position = (position[0] - 1, position[1])
            else:
                position = (position[0], position[1] - 1)


    print(f"Number of steps: {numbersOfSteps}")

def main():
    parseInput()
    findGuardPath()

if __name__ == "__main__":
    main()