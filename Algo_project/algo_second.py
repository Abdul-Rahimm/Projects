import tkinter as tk
from tkinter import Canvas
import time

# Function to check if lines intersect
def check_intersection(a, b, c, d):
    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # Collinear
        return 1 if val > 0 else 2  # Clockwise or counterclockwise

    def on_segment(p, q, r):
        return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
                q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

    o1 = orientation(a, b, c)
    o2 = orientation(a, b, d)
    o3 = orientation(c, d, a)
    o4 = orientation(c, d, b)

    if o1 != o2 and o3 != o4:
        return True, None  # Lines intersect

    # Special cases for collinear lines
    if o1 == 0 and on_segment(a, c, b):
        return True, (c[0], c[1])  # Intersection point is c
    if o2 == 0 and on_segment(a, d, b):
        return True, (d[0], d[1])  # Intersection point is d
    if o3 == 0 and on_segment(c, a, d):
        return True, (a[0], a[1])  # Intersection point is a
    if o4 == 0 and on_segment(c, b, d):
        return True, (b[0], b[1])  # Intersection point is b

    return False, None  # No intersection

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
