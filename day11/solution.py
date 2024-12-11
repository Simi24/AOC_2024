# - If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# - If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
#   The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.
#   (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# - If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.

stones = []

def parseInput():
    with open("input.txt") as file:
        for line in file:
            stones.extend([int(x) for x in line.strip().split()])
        
        print(stones)

def stonesAfterNSeconds(n):
    global stones
    for i in range(n):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.extend([1])
            elif len(str(stone)) % 2 == 0:
                half = len(str(stone)) // 2
                new_stones.extend([int(str(stone)[:half]), int(str(stone)[half:])])
            else:
                new_stones.extend([stone * 2024])
        stones = new_stones
        # print(stones)
    return stones

def main():
    global stones
    parseInput()
    stonesAfterNSeconds(75)
    print(len(stones))


if __name__ == "__main__":
    main()