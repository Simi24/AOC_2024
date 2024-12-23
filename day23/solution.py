import networkx
from collections import defaultdict
import matplotlib.pyplot as plt
from itertools import combinations

edges = []


def parse_input():
    with open("input.txt") as file:
        lines = file.readlines()
        for line in lines:
            _edge = line.split("-")
            edges.append((_edge[0], _edge[1].strip()))


def create_graph():
    G = networkx.Graph()
    G.add_edges_from(edges)
    return G


def draw_graph(G):
    plt.figure(figsize=(10, 8))
    networkx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=3000, font_size=10)
    plt.show()


def find_triplets_nx(G):
    triplets = []
    for triplet in combinations(G.nodes, 3):
        if (
            G.has_edge(triplet[0], triplet[1])
            and G.has_edge(triplet[0], triplet[2])
            and G.has_edge(triplet[1], triplet[2])
        ):
            triplets.append(triplet)
    return triplets


def find_max_clique_nx(G):
    return max(networkx.find_cliques(G), key=len)


def filter_triplets(triplets):
    return [triplet for triplet in triplets if any(node.startswith("t") for node in triplet)]


def main():
    parse_input()
    G = create_graph()
    triplets = find_triplets_nx(G)
    filtered_triplets = filter_triplets(triplets)
    # Part 1
    print(len(filtered_triplets))
    max_clique = find_max_clique_nx(G)
    # Part 2
    print(",".join(sorted(max_clique)))


if __name__ == "__main__":
    main()
