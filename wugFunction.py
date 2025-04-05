import matplotlib.pyplot as plt
import numpy as np

def bezier_curve(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Calculates points on a cubic Bézier curve.

    Args:
        x1, y1: Coordinates of the first control point.
        x2, y2: Coordinates of the second control point.
        x3, y3: Coordinates of the third control point.
        x4, y4: Coordinates of the fourth control point.

    Returns:
        A list of (x, y) points on the curve.
    """

    t_values = np.linspace(0, 1, 100)  # Generate 100 t values
    x_values = []
    y_values = []

    for t in t_values:
        x = (1-t)**3*x1 + 3*(1-t)**2*t*x2 + 3*(1-t)*t**2*x3 + t**3*x4
        y = (1-t)**3*y1 + 3*(1-t)**2*t*y2 + 3*(1-t)*t**2*y3 + t**3*y4
        x_values.append(x)
        y_values.append(y)

    return x_values, y_values

# Example Usage
x1, y1 = 10, 0
x2, y2 = 40, 0
x3, y3 = 0, 25
x4, y4 = 60, 17
x_points1, y_points1 = bezier_curve(x1, y1, x2, y2, x3, y3, x4, y4)

# Second curve control points
a1, b1 = 10, 0
a2, b2 = 80, -5
a3, b3 = 38, 17
a4, b4 = 60, 17
x_points2, y_points2 = bezier_curve(a1, b1, a2, b2, a3, b3, a4, b4)

#leg left
i1, j1 = 33, 1
i2, j2 = 32, -3
i3, j3 = 30, -4
i4, j4 = 29, -4.5
x_points3, y_points3 = bezier_curve(i1, j1, i2, j2, i3, j3, i4, j4)

#leg right
h1, k1 = 45, 0.5
h2, k2 = 46, -1
h3, k3 = 47, -3.5
h4, k4 = 45, -4.5
x_points4, y_points4 = bezier_curve(h1, k1, h2, k2, h3, k3, h4, k4)

#leg foot
q1, p1 = 26.5, -4.5
q2, p2 = 29, -4.6
q3, p3 = 33, -4
q4, p4 = 35, -4.5
x_points5, y_points5 = bezier_curve(q1, p1, q2, p2, q3, p3, q4, p4)

#right foot
w1, z1 = 45, -4.5
w2, z2 = 48, -4.5
w3, z3 = 52, -4.3
w4, z4 = 53, -4.5
x_points6, y_points6 = bezier_curve(w1, z1, w2, z2, w3, z3, w4, z4)


# Plot the curve
plt.plot(x_points1, y_points1, label='Curve 1', color='blue')
plt.plot(x_points2, y_points2, label='Curve 2', color='green')
plt.plot(x_points3, y_points3, label='Leg Left', color='purple')
plt.plot(x_points4, y_points4, label='Leg Right', color='navy')
plt.plot(x_points5, y_points5, label='Leg Right', color='blueviolet')
plt.plot(x_points6, y_points6, label='Leg Right', color='royalblue')
plt.scatter([x1, x2, x3, x4], [y1, y2, y3, y4], color='red', marker='o')  # Plot control
plt.scatter([a1, a2, a3, a4], [b1, b2, b3, b4], color='orange', label='Curve 2 Control Points')
plt.scatter([i1, i2, i3, i4], [j1, j2, j3, j4], color='pink', marker='o')
plt.scatter([h1, h2, h3, h4], [k1, k2, k3, k4], color='grey', marker='o') # Plot control
plt.scatter([q1, q2, q3, q4], [p1, p2, p3, p4], color='blueviolet', label='o')
plt.scatter([w1, w2, w3, w4], [z1, z2, z3, z4], color='royalblue', label='o')


# Add solid circle
circle = plt.Circle((45, 13), 1, color='black', alpha=1)  # Circle with center (40, 30) and radius 15
plt.gca().add_patch(circle)

# points
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Cubic Bézier Curve")
plt.grid(True)
plt.show()