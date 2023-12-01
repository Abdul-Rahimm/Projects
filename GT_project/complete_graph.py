import tkinter as tk
import math

class GraphApp:
    def _init_(self, root, vertices):
        self.canvas = tk.Canvas(root, width=600, height=600, bg='white')
        self.canvas.pack()
        self.vertices = vertices
        self.vertex_coords = []
        self.draw_complete_graph()

    def draw_complete_graph(self):
        # Calculate positions of vertices in a circle
        angle = 2 * math.pi / self.vertices
        for i in range(self.vertices):
            x = 300 + 200 * math.cos(i * angle)
            y = 300 + 200 * math.sin(i * angle)
            self.vertex_coords.append((x, y))
            self.draw_vertex(x, y, str(i))

        # Draw edges between all pairs of vertices
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                self.draw_edge(self.vertex_coords[i], self.vertex_coords[j])

    def draw_vertex(self, x, y, vertex_id):
        self.canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill='blue')
        self.canvas.create_text(x, y, text=vertex_id, fill='white')

    def draw_edge(self, start_pos, end_pos):
        self.canvas.create_line(start_pos[0], start_pos[1], end_pos[0], end_pos[1], fill='black')

if __name__ == '_main_':
    root = tk.Tk()
    root.title("Complete Graph Visualization")

    # Number of vertices for the complete graph
    num_vertices = 60  # Change this value as needed

    app = GraphApp(root, num_vertices)
    root.mainloop()