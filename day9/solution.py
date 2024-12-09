blocks = []

def parseInput():
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            index = 0
            for i in range(len(line.strip())):
                if i % 2 == 0:
                    n = int(line[i])
                    while n > 0:
                        blocks.append(index)
                        n -= 1
                    index += 1
                else:
                    n = int(line[i])
                    while n > 0:
                        blocks.append(".")
                        n -= 1
                    


def reorderBlocks():
    l, r = 0, len(blocks) - 1

    while l < r:
        if blocks[r] == ".":
            r -= 1
        elif blocks[l] != "." and blocks[r] != ".":
            l += 1
        elif (blocks[l] != "." and blocks[r] == ".") or (blocks[l] == "." and blocks[r] != "."): 
            blocks[l], blocks[r] = blocks[r], blocks[l]
            l += 1
            r -= 1
    
    print(blocks)

def findChecksum():
    ret = 0

    for i in range(len(blocks)):
        if blocks[i] != ".":
            ret += blocks[i] * i
    
    return ret

def main():
    parseInput()
    reorderBlocks()
    print(findChecksum())

if __name__ == "__main__":
    main()