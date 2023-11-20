import turtle
import numpy as np


def orientation(a, b, c):
    ans = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    if ans == 0:
        return 0
    elif ans > 0:
        return 1
    else:
        return 2

def polar_angle(p, q):
    y_diff = q[1] - p[1]
    x_diff = q[0] - p[0]
    return np.arctan2(y_diff, x_diff)

def distance(p, q):
    return np.sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1])** 2)

def draw_lines(current_vertex, next_Vertex):
    turtle.penup()
    turtle.goto(current_vertex)
    turtle.pendown()
    turtle.color('red')
    turtle.setheading(turtle.towards(next_Vertex))
    turtle.forward(turtle.distance(next_Vertex))
    turtle.penup()

def erase_line(current_vertex, next_Vertex):
    turtle.penup()
    turtle.goto(current_vertex)
    turtle.pendown()
    turtle.color('white')
    turtle.setheading(turtle.towards(next_Vertex))
    turtle.forward(turtle.distance(next_Vertex))
    turtle.penup()

def grahamScan(points):
    reference_point = min(points, key=lambda point: (point[1], point[0]))
    sorted_points = sorted(points,
                           key=lambda point: (polar_angle(reference_point, point), distance(reference_point, point)))
    
    if len(points) < 3:
        return "Convex hull can't be formed with less than 3 points"
    
    stack = []
    stack.append(sorted_points[0])
    draw_lines(sorted_points[0], sorted_points[1])
    stack.append(sorted_points[1])
    stack.append(sorted_points[2])
    draw_lines(sorted_points[1], sorted_points[2])
    
    for i in range(3, len(points)):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], sorted_points[i]) != 2:
            erase_line(stack[-1], stack[-2])
            stack.pop()
        stack.append(sorted_points[i])
        draw_lines(stack[-2], sorted_points[i])
    draw_lines(stack[-1], sorted_points[0])
    return stack

def setGraph(points):
    turtle.speed(0)
    turtle.hideturtle()

    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()
    turtle.forward(400)

    turtle.penup()
    turtle.goto(0, -200)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(400)

    turtle.penup()
    for point in points:
        turtle.goto(point)
        turtle.dot(5, 'black')

points = [(30, 60), (0, 0), (90, 20), (160, 100), (30, 150), (70, 70), (130, 70), (130, 130)]
setGraph(points)
grahamScan(points)
turtle.done()