import tkinter as tk
from tkinter import Canvas
import time

def parametric_equation(p, q, t):
    return (1 - t) * p[0] + t * q[0], (1 - t) * p[1] + t * q[1]

def check_intersection(a, b, c, d):
    def on_segment(p, q, r):
        return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

    for t in [0.0, 0.25, 0.5, 0.75, 1.0]:
        intersection_point = parametric_equation(a, b, t)
        if on_segment(a, intersection_point, b) and on_segment(c, intersection_point, d):
            return True, intersection_point

    return False, None

# Function to get user input via mouse clicks
def get_coordinates():
    root = tk.Tk()
    root.title('Click on the Canvas to Enter Points')

    canvas = Canvas(root, width=500, height=500)
    canvas.pack()

    coordinates = []

    def on_click(event):
        nonlocal coordinates
        x, y = event.x, event.y
        print(f"Clicked at ({x}, {y})")
        coordinates.append((x, y))
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill='red')  # Mark the point

        if len(coordinates) == 2:
            canvas.create_line(coordinates[0][0], coordinates[0][1], coordinates[1][0], coordinates[1][1], fill='blue', width=2)

        if len(coordinates) == 4:
            canvas.create_line(coordinates[2][0], coordinates[2][1], coordinates[3][0], coordinates[3][1], fill='green', width=2)
            root.after(2000, root.destroy)  # Close the window after 2 seconds

    canvas.bind("<Button-1>", on_click)

    root.mainloop()

    return coordinates

# Get input coordinates from the user
user_coordinates = get_coordinates()

# Check if lines intersect
intersect, intersection_point = check_intersection(user_coordinates[0], user_coordinates[1],
                                                   user_coordinates[2], user_coordinates[3])

# Report the result
if intersect:
    print("Lines intersect.")
else:
    print("Lines do not intersect.")
