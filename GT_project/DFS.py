import tkinter as tk
import math
from collections import defaultdict

class GraphVisualization:
    def _init_(self, edges):
        self.edges = edges
        self.graph = defaultdict(list)
        self.build_graph()
        self.start_dfs_visualization()

    def build_graph(self):
        for start, end in self.edges:
            self.graph[start].append(end)
            self.graph[end].append(start)  # Assuming undirected graph

    def start_dfs_visualization(self):
        self.root = tk.Tk()
        self.root.title("DFS Visualization")
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='white')
        self.canvas.pack()
        self.dfs(2)

    def draw_graph(self, position, dfs_edges, visited):
        self.canvas.delete("all")

        # Draw edges
        for start, ends in self.graph.items():
            for end in ends:
                if start > end:  # Avoid double drawing
                    continue
                x1, y1 = position[start]
                x2, y2 = position[end]
                color = "red" if (start, end) in dfs_edges or (end, start) in dfs_edges else "black"
                self.canvas.create_line(x1, y1, x2, y2, fill=color, width=2)

        # Draw nodes
        for node in self.graph:
            x, y = position[node]
            color = 'green' if node in visited else 'white'
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill=color, outline="black")
            self.canvas.create_text(x, y, text=str(node))

        self.root.update()

    def dfs_util(self, v, visited, dfs_edges):
        visited.add(v)

        for neighbour in self.graph[v]:
            if neighbour not in visited:
                dfs_edges.add((v, neighbour))
                self.dfs_util(neighbour, visited, dfs_edges)

    def dfs(self, start_node):
        visited = set()
        dfs_edges = set()

        # Position nodes in a circle
        position = {}
        center_x, center_y = 400, 300
        radius = 200
        total_nodes = len(self.graph)
        angle = 2 * math.pi / total_nodes

        for i, node in enumerate(self.graph):
            x = center_x + radius * math.cos(i * angle)
            y = center_y + radius * math.sin(i * angle)
            position[node] = (x, y)

        self.dfs_util(start_node, visited, dfs_edges)
        self.draw_graph(position, dfs_edges, visited)
        self.root.mainloop()

edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
GraphVisualization(edges)