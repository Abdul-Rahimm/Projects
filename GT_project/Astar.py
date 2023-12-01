import networkx as nx
import matplotlib.pyplot as plt
import time

def visualize_graph(graph, path_edges=[], src=None, goal=None):
    pos = nx.shell_layout(graph)  # Using shell layout for a circular appearance
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

    labels = {}
    if src:
        labels[src] = 'src'
    if goal:
        labels[goal] = 'goal'

    pos_labels = {key: (pos[key][0], pos[key][1] + 0.1) for key in pos}  # Adjust label position
    nx.draw_networkx_labels(graph, pos_labels, labels, font_color='red', font_size=10)

    edge_labels = {(edge[0], edge[1]): graph[edge[0]][edge[1]]['weight'] for edge in graph.edges}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='green')

    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='r', width=2)

    plt.draw()
    plt.pause(1)  # Pause to visualize each step


def A_star(graph, start, goal):
    open_set = set([start])
    closed_set = set()
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph.nodes}
    f_score[start] = heuristic(start, goal)

    visualize_graph(graph, src=start, goal=goal)

    while open_set:
        current = min(open_set, key=lambda node: f_score[node])

        if current == goal:
            return True  # Path found

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in graph.neighbors(current):
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + graph[current][neighbor]['weight']

            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g_score >= g_score[neighbor]:
                continue

            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
            visualize_graph(graph, path_edges=[(current, neighbor)], src=start, goal=goal)

    return False  # No path found

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def main():
    graph = nx.Graph()

    nodes = [(0, 0), (1, 2), (3, 1), (4, 3), (5, 0), (7, 2), (6, 5), (9, 4), (8, 7), (10, 6), (12, 5), (11, 8)]

    for node in nodes:
        graph.add_node(node)

    edges = [
        ((0, 0), (1, 2), 2),
        ((1, 2), (3, 1), 3),
        ((3, 1), (4, 3), 2),
        ((4, 3), (5, 0), 4),
        ((5, 0), (7, 2), 3),
        ((7, 2), (6, 5), 2),
        ((6, 5), (9, 4), 3),
        ((9, 4), (8, 7), 4),
        ((8, 7), (10, 6), 2),
        ((10, 6), (12, 5), 3),
        ((12, 5), (11, 8), 4),
        ((11, 8), (9, 4), 3),
        ((1, 2), (6, 5), 4),
        ((5, 0), (8, 7), 5),
        ((11, 8), (7, 2), 6)
    ]

    for edge in edges:
        graph.add_edge(edge[0], edge[1], weight=edge[2])

    visualize_graph(graph, src=(0, 0), goal=(12, 5))

    start = (0, 0)
    goal = (12, 5)

    if A_star(graph, start, goal):
        print("Path found!")
    else:
        print("No path found!")

    plt.show()

if __name__ == "__main__":
    main()
