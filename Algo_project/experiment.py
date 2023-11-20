from matplotlib import pyplot as plt
from random import randint

def create_points(ct, min=0, max=50):
    return [[randint(min, max), randint(min, max)] for _ in range(ct)]

def scatter_plot(coords, convex_hull=None):
    xs, ys = zip(*coords)
    plt.scatter(xs, ys)

    if convex_hull is not None:
        for i in range(len(convex_hull)):
            c0 = convex_hull[i]
            c1 = convex_hull[(i + 1) % len(convex_hull)]
            plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'r')
    
    plt.show()

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or Counterclockwise

def monotone_chain(points, show_progress=False):
    n = len(points)
    if n < 3:
        print("Convex hull not possible with less than 3 points.")
        return None

    points.sort()  # Sort points lexicographically

    upper_hull = []
    for p in points:
        while len(upper_hull) >= 2 and orientation(upper_hull[-2], upper_hull[-1], p) != 1:
            upper_hull.pop()
        upper_hull.append(p)

        if show_progress:
            scatter_plot(points, upper_hull)

    lower_hull = []
    for p in reversed(points):
        while len(lower_hull) >= 2 and orientation(lower_hull[-2], lower_hull[-1], p) != 1:
            lower_hull.pop()
        lower_hull.append(p)

        if show_progress:
            scatter_plot(points, lower_hull)

    convex_hull = upper_hull[:-1] + lower_hull[:-1]

    if show_progress:
        scatter_plot(points, convex_hull)

    return convex_hull

# Example usage
pts = create_points(10)
print("Points:", pts)
convex_hull = monotone_chain(pts, show_progress=True)
print("Convex Hull:", convex_hull)
scatter_plot(pts, convex_hull)
