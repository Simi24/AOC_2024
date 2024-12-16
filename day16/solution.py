import networkx as nx

grid = []
movements = []
initial_position = (0, 0)
desination = (0, 0)

def parse_input():
    global grid
    global movements
    global initial_position
    global desination
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            grid.append(list(line.strip()))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "S":
                    initial_position = (j, i)
                elif grid[i][j] == "E":
                    desination = (j, i)
        
        print(f"Initial position: {initial_position}")
        print(f"Desination: {desination}")
        print("\n".join("".join(row) for row in grid))

def build_graph_with_weights(labyrinth):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Nord, Sud, Ovest, Est
    direction_names = ['N', 'S', 'W', 'E']
    rows, cols = len(labyrinth), len(labyrinth[0])
    
    G = nx.DiGraph()
    
    for x in range(rows):
        for y in range(cols):
            if labyrinth[x][y] != '#':
                for i, (dx, dy) in enumerate(directions):
                    next_x, next_y = x + dx, y + dy
                    
                    if 0 <= next_x < rows and 0 <= next_y < cols and labyrinth[next_x][next_y] != '#':
                        G.add_edge((x, y, direction_names[i]), (next_x, next_y, direction_names[i]), weight=1)
                        
                        for j, dir_name in enumerate(direction_names):
                            if i != j:
                                G.add_edge((x, y, direction_names[j]), (next_x, next_y, direction_names[i]), weight=1001)
    return G

def find_shortest_path_with_networkx(labyrinth, start, end):
    directions = ['N', 'S', 'W', 'E']  # Direzioni iniziali possibili
    
    G = build_graph_with_weights(labyrinth)
    
    min_cost = float('inf')
    for direction in directions:
        try:
            cost = nx.shortest_path_length(
                G,
                source=(start[0], start[1], direction),
                target=(end[0], end[1], direction),
                weight="weight"
            )
            min_cost = min(min_cost, cost)
        except nx.NetworkXNoPath:
            continue
    
    return min_cost if min_cost < float('inf') else -1

def find_all_shortest_paths_with_networkx(labyrinth, start, end):
    initial_direction = 'E'
    
    G = build_graph_with_weights(labyrinth)
    
    source_node = (start[0], start[1], initial_direction)
    
    target_nodes = [
        (end[0], end[1], dir_name) for dir_name in ['N', 'S', 'W', 'E']
    ]
    
    if source_node not in G.nodes:
        return []
    
    all_paths = []
    for target_node in target_nodes:
        try:
            paths = list(nx.all_shortest_paths(
                G,
                source=source_node,
                target=target_node,
                weight="weight"
            ))
            all_paths.extend(paths)
        except nx.NetworkXNoPath:
            continue
    
    unique_tiles = set()

    for path in all_paths:
        for tile in path:
            unique_tiles.add((tile[0], tile[1]))
    
    print(f"Unique tiles: {len(unique_tiles)}")
    
    if all_paths:
        return all_paths
    else:
        return []
    

def main():
    global grid
    global initial_position
    global desination

    parse_input()
    print(f"Path cost with NetworkX: {find_shortest_path_with_networkx(grid, initial_position, desination)}")
    print(f"Paths: {len(find_all_shortest_paths_with_networkx(grid, initial_position, desination))}")

if __name__ == "__main__":
    main()