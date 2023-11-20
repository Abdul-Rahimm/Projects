import turtle
import math

def graham_scan(points):
    def polar_angle(p1, p2):
        return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

    def distance(p1, p2):
        return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0  # Collinear
        return 1 if val > 0 else 2  # Clockwise or counterclockwise

    def graham_scan_algorithm(points):
        if len(points) < 3:
            return points

        hull = []

        # Find the point with the lowest y-coordinate (and leftmost if tied)
        pivot = min(points, key=lambda point: (point[1], point[0]))

        # Sort the points based on polar angle from the pivot
        sorted_points = sorted(points, key=lambda point: (polar_angle(pivot, point), distance(pivot, point)))

        # Initialize the convex hull with the pivot and the first two sorted points
        hull = [pivot, sorted_points[0], sorted_points[1]]

        # Iterate through the remaining points
        for point in sorted_points[2:]:
            while len(hull) > 1 and orientation(hull[-2], hull[-1], point) != 2:
                hull.pop()
            hull.append(point)

        return hull

    convex_hull = graham_scan_algorithm(points)
    return convex_hull
# Function to draw a point at a given position
def draw_point(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(5)  # Draw a small dot at the specified position

# Function to draw a line between two points
def draw_line(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

def write_text(text, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(text, align="center")
# Set up the turtle screen
screen = turtle.Screen()
screen.title("Graham Scan Convex Hull")
screen.bgcolor("white")

# Draw coordinate axes
draw_line(-200, 0, 200, 0)
write_text("X", 200, 0)
for i in range(0, 201, 20):
    draw_line(i, -5, i, 5)
    write_text(str(i), i, -20)

for i in range(-150, 200, 20):
    draw_line(-5, i, 5, i)
    write_text(str(i), -20, i)

draw_line(0, -200, 0, 200)
write_text("Y", 0, 200)

# Input the number of points
num_points = int(input("Enter the number of points to plot: "))

# Input points through the GUI
points = []

def register_click(x, y):
    points.append((x, y))
    draw_point(x, y)
    
    if len(points) == num_points:
        write_text("All points plotted! Close the window manually.", 0, 220)
        convex_hull = graham_scan(points)
        
        # Draw convex hull
        for i in range(len(convex_hull)):
            draw_line(*convex_hull[i], *convex_hull[(i + 1) % len(convex_hull)])

        screen.onscreenclick(None)  # Unregister the click event handler

# Register the click event
screen.onscreenclick(register_click)

# Wait for the user to click num_points times
turtle.mainloop()

# Close the turtle graphics window on click
screen.exitonclick()
