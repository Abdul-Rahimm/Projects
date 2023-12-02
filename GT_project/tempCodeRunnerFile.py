def A_star(graph, start, goal):
    open_set = set([start])
    closed_set = set()
    g_score = {node: float('inf') for node in graph.nodes} 
    # function g
    g_score[start] = 0
    # function f
    f_score = {node: float('inf') for node in graph.nodes}
    f_score[start] = heuristic(start, goal)

    visualize_graph(graph, src=start, goal=goal)

    while open_set:
        current = min(open_set, key=lambda node: f_score[node])

        if current == goal:
            return True  # Path found

        open_set.remove(current)
        # open set means exploring wale nodes
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
