blocks = []
occurrences = {}
spaces = {}
_line = ""

def parseInput():
    global _line
    with open("inputTest.txt") as file:
        lines = file.readlines()
        for line in lines:
            _line = line
            process_line(line)

def process_line(line):
    blocks = []
    occurrences = {}
    spaces = {}

    index = 0
    indexSpaces = 0
    for i in range(len(line.strip())):
        if i % 2 == 0:
            n = int(line[i])
            while n > 0:
                blocks.append(index)
                n -= 1
            index += 1
        else:
            spaces[indexSpaces] = int(line[i])
            n = int(line[i])
            while n > 0:
                blocks.append(".")
                n -= 1
            indexSpaces += 1

    index = len(line) // 2
    for i in range(len(line)-1, -1, -1):
        if i % 2 == 0:
            occurrences[index] = int(line[i])
            index -= 1

    print(blocks)
    print(occurrences)
    print(spaces)

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

def findChecksum():
    ret = 0

    for i in range(len(blocks)):
        if blocks[i] != ".":
            ret += blocks[i] * i
    
    return ret

def reorderBlocks2():
    line = [int(n) for n in _line.strip()]
    print(line)
    occurrence = []
    
    #move to the right to the left
    for i in range(len(line)-1, -1, -1):
        if i % 2 == 0:
            
            #move to left from right to find a space
            for j in range(len(line)):
                
                if j % 2 != 0:
                    if line[i] <= line[j]:
                        print("elemento da fittare ", line[i])
                        print("spazio trovato ",line[j])
                        print("indice spazio ", j)
                        for n in range(line[i]):
                            occurrence.append(i//2)
                        line[j] -= line[i]
                        line[i] = 0
                        print(line)
                        break
    
    print(line)
    print(occurrence)

    s = ''.join(str(x) for x in line)
    print(s)
    print(process_line(s))
    

def main():
    parseInput()
    #reorderBlocks()
    #print(findChecksum())
    reorderBlocks2()

if __name__ == "__main__":
    main()