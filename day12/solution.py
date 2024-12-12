matrix = []
rows = 0
cols = 0

def parseInput():
    global matrix, rows, cols
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            row = list(line.strip())
            matrix.append(row)
    rows = len(matrix)
    cols = len(matrix[0])

def findTotalPriceFences():
    global matrix, rows, cols
    
    def dfs(i, j, visited, target):
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[i][j] != target or (i, j) in visited:
            return 0, 0
        
        visited.add((i, j))
        area = 1
        perimeter = 4

        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] == target:
                perimeter -= 1

        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            sub_area, sub_perimeter = dfs(ni, nj, visited, target)
            area += sub_area
            perimeter += sub_perimeter

        return area, perimeter

    visited = set()
    gardens = 0
    fencesCost = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                area, perimeter = dfs(i, j, visited, matrix[i][j])
                fencesCost += area * perimeter
                gardens += 1
    
    print(fencesCost)
    return fencesCost


def main():
    parseInput()
    findTotalPriceFences()

if __name__ == "__main__":
    main()