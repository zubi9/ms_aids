# -*- coding: utf-8 -*-
"""logistic maps and fractals.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YVRQJDina9NCkFr8ygBU3e3K9mG3VuHF
"""

import warnings
# To ignore all warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt

# Define the logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
r_values = np.linspace(2.4, 4.0, 10000)  # Range of r values
iterations = 1000  # Number of iterations for each r value
last_iterations = 100  # Number of iterations to display in the bifurcation diagram

# Arrays to store the r values and corresponding x values
r_list = []
x_list = []

# Iterate over each r value and create the bifurcation diagram
for r in r_values:
    x = 0.5  # Initial condition
    for _ in range(iterations):
        x = logistic_map(r, x)
        if iterations - last_iterations < _:
            r_list.append(r)
            x_list.append(x)

# Create the bifurcation diagram
plt.figure(figsize=(12, 6))
plt.plot(r_list, x_list, ',k', alpha=0.25)
plt.xlim(2.4, 4.0)
plt.ylim(0, 1)
plt.xlabel('r')
plt.ylabel('x')
plt.title('Bifurcation Diagram of the Logistic Map')
plt.show()

!pip install mpld3

import numpy as np
import matplotlib.pyplot as plt
import mpld3

# Define the logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
r_values = np.linspace(2.4, 4.0, 4000)  # Range of r values
iterations = 1000  # Number of iterations for each r value
last_iterations = 100  # Number of iterations to display in the bifurcation diagram

# Arrays to store the r values and corresponding x values
r_list = []
x_list = []

# Iterate over each r value and create the bifurcation diagram
for r in r_values:
    x = 0.5  # Initial condition
    for _ in range(iterations):
        x = logistic_map(r, x)
        if iterations - last_iterations < _:
            r_list.append(r)
            x_list.append(x)

# Create the bifurcation diagram
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(r_list, x_list, ',k', alpha=0.25)
ax.set_xlim(2.4, 4.0)
ax.set_ylim(0, 1)
ax.set_xlabel('r')
ax.set_ylabel('x')
ax.set_title('Bifurcation Diagram of the Logistic Map')

# Enable interactive mode with mpld3
mpld3.display(fig)

import numpy as np
import matplotlib.pyplot as plt
import mpld3

# Define the logistic map function
def logistic_map(r, x):
    return r * x * (1 - x)

# Parameters
r_values = np.linspace(2.4, 4.0, 100000)  # Reduce the number of r values
iterations = 500  # Reduce the number of iterations for each r value
last_iterations = 100  # Number of iterations to display in the bifurcation diagram

# Arrays to store the r values and corresponding x values
r_list = []
x_list = []

# Iterate over each r value and create the bifurcation diagram
for r in r_values:
    x = 0.5  # Initial condition
    for _ in range(iterations):
        x = logistic_map(r, x)
        if iterations - last_iterations < _:
            r_list.append(r)
            x_list.append(x)

# Create the bifurcation diagram
fig, ax = plt.subplots(figsize=(8, 4))  # Reduce the figure size
ax.plot(r_list, x_list, ',k', alpha=0.25)
ax.set_xlim(2.4, 4.0)
ax.set_ylim(0, 1)
ax.set_xlabel('r')
ax.set_ylabel('x')
ax.set_title('Bifurcation Diagram of the Logistic Map')

# Enable interactive mode with mpld3
# mpld3.display(fig)
plt.show()

import matplotlib.pyplot as plt

# Function to generate the Cantor set
def generate_cantor_set(start, end, depth):
    if depth == 0:
        return [(start, end)]
    else:
        one_third = (2 * start + end) / 3
        two_third = (start + 2 * end) / 3
        segments = generate_cantor_set(start, one_third, depth - 1) + generate_cantor_set(two_third, end, depth - 1)
        return segments

# Function to visualize the Cantor set
def visualize_cantor_set(segments):
    fig, ax = plt.subplots()
    for segment in segments:
        ax.plot([segment[0], segment[1]], [0, 0], color='b', linewidth=4)

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.1, 0.1)
    ax.axis('off')
    plt.show()

# Parameters
start = 0
end = 1
depth = 5  # Increase for more iterations (higher depth)

# Generate and visualize the Cantor set
cantor_set = generate_cantor_set(start, end, depth)
visualize_cantor_set(cantor_set)

import matplotlib.pyplot as plt

# Function to generate Cantor dust
def generate_cantor_dust(x, y, size, depth, ax):
    if depth == 0:
        ax.add_patch(plt.Rectangle((x, y), size, size, color='b'))
    else:
        new_size = size / 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue  # Skip the middle square
                generate_cantor_dust(x + i * new_size, y + j * new_size, new_size, depth - 1, ax)

# Create a figure
fig, ax = plt.subplots()

# Parameters
x = 0
y = 0
size = 1
depth = 3  # Adjust the depth for more iterations (higher detail)

# Generate Cantor dust
generate_cantor_dust(x, y, size, depth, ax)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')
ax.set_title('Cantor Dust')

plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Function to generate the Cantor set
def generate_cantor_set_3d(x1, x2, y, depth, ax):
    if depth == 1:
        ax.plot([x1, x2], [y, y], [1, 1], color='b', linewidth=1)
    else:
        one_third = (2 * x1 + x2) / 3
        two_third = (x1 + 2 * x2) / 3
        generate_cantor_set_3d(x1, one_third, y - 0.1, depth - 1, ax)
        generate_cantor_set_3d(two_third, x2, y - 0.1, depth - 1, ax)

# Create a 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Parameters
x1 = 0
x2 = 1
y = 0
depth = 5  # Adjust the depth for more iterations (higher detail)

# Generate the Cantor set in 3D
generate_cantor_set_3d(x1, x2, y, depth, ax)

ax.set_xlim(0, 1)
ax.set_ylim(-0.5, 0)
ax.set_zlim(0, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Cantor Ternary Set')

plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Function to generate the Koch snowflake
def koch_snowflake(order, scale=10):
    if order == 0:
        # Base case: a straight line segment
        return [(0, 0), (1, 0)]
    else:
        # Recursive case: generate the snowflake for the previous order
        snowflake = koch_snowflake(order - 1, scale)
        new_snowflake = []
        for p1, p2 in zip(snowflake[:-1], snowflake[1:]):
            x1, y1 = p1
            x2, y2 = p2
            x = x2 - x1
            y = y2 - y1
            # Calculate 1/3 and 2/3 points
            p1 = (x1, y1)
            p3 = (x1 + x / 3, y1 + y / 3)
            p4 = (x1 + x / 3 + np.cos(np.pi / 3) * y / 3, y1 + x / 3 * np.sin(np.pi / 3) + y / 3)
            p5 = (x1 + 2 * x / 3, y1 + 2 * y / 3)
            p6 = (x2, y2)
            new_snowflake.extend([p1, p3, p4, p5])
        new_snowflake.append(p6)
        return new_snowflake

# Create and visualize the Koch snowflake
order = 6  # Adjust the order for more iterations (higher detail)
snowflake = koch_snowflake(order)
x, y = zip(*snowflake)

plt.figure(figsize=(12, 6))
plt.plot(x, y, 'b')
plt.axis('equal')
plt.axis('off')
plt.title(f'Koch Snowflake (Order {order})')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Function to generate the Koch snowflake for an equilateral triangle
def koch_snowflake_triangle(order, scale=10):
    if order == 0:
        # Base case: a straight equilateral triangle
        return [(0, 0), (scale, 0), (scale / 2, scale * np.sin(np.pi / 3))]
    else:
        # Recursive case: generate the snowflake for the previous order
        snowflake = koch_snowflake_triangle(order - 1, scale)
        new_snowflake = []
        for i in range(len(snowflake)):
            p1 = snowflake[i]
            p2 = snowflake[(i + 1) % len(snowflake)]
            x1, y1 = p1
            x2, y2 = p2
            x = x2 - x1
            y = y2 - y1
            # Calculate 1/3 and 2/3 points
            p3 = (x1 + x / 3, y1 + y / 3)
            p5 = (x1 + 2 * x / 3, y1 + 2 * y / 3)
            p4 = (p3[0] + np.cos(np.pi / 3) * (p5[0] - p3[0]), p3[1] + np.sin(np.pi / 3) * (p5[0] - p3[0]))
            new_snowflake.extend([p1, p3, p4, p5])
        return new_snowflake

# Create and visualize the Koch snowflake for an equilateral triangle
order = 3  # Adjust the order for more iterations (higher detail)
snowflake_triangle = koch_snowflake_triangle(order)
x, y = zip(*snowflake_triangle)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b')
plt.axis('equal')
plt.axis('off')
plt.title(f'Koch Snowflake for Equilateral Triangle (Order {order})')
plt.show()

import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

# Parameters
N = 100  # Number of sites
t1 = 1.0  # Hopping parameter
phi = (1 + np.sqrt(5)) / 2  # Golden ratio

# Generate Fibonacci sequence
fibonacci_seq = [0, 1]
while len(fibonacci_seq) < N:
    next_val = fibonacci_seq[-1] + fibonacci_seq[-2]
    fibonacci_seq.append(next_val)

# Create the Fibonacci Hamiltonian matrix
Hamiltonian = np.zeros((N, N), dtype=complex)
for i in range(N):
    Hamiltonian[i, i] = i * t1
    if i < N - 1:
        Hamiltonian[i, i + 1] = -t1
    if i > 0:
        Hamiltonian[i, i - 1] = -t1

# Diagonalize the Hamiltonian
eigenvalues, eigenvectors = np.linalg.eigh(Hamiltonian)

# Plot the spectrum
plt.figure(figsize=(8, 6))
plt.plot(range(N), eigenvalues, 'bo')
plt.xlabel('Eigenvalue Index')
plt.ylabel('Energy')
plt.title('Spectrum of Fibonacci Hamiltonian')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# Function to generate Peano curve for a "U" shape line
def peano_curve_u_shape(order, points):
    if order == 0:
        return points
    else:
        new_points = []
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            dx = (x2 - x1) // 3
            dy = (y2 - y1) // 3
            p1 = (x1, y1)
            p2 = (x1 + dx, y1 + dy)
            p3 = (x1 + dx * 2, y1 + dy * 2)
            p4 = (x1 + dx * 3, y1 + dy * 3)
            new_points.extend([p1, p2, p3, p4])
        new_points.append(points[-1])
        return peano_curve_u_shape(order - 1, new_points)

# Initial points for the "U" shape line
points = [(0, 0), (1, 0)]

# Generate Peano curve for the "U" shape line
order = 4  # Adjust the order for more iterations (higher detail)
peano_points = peano_curve_u_shape(order, points)
x, y = zip(*peano_points)

# Plot the Peano curve applied to the "U" shape line
plt.figure(figsize=(6, 6))
plt.plot(x, y, color='b', linewidth=2)
plt.title(f'Peano Curve Applied to "U" Shape Line (Order {order})')
plt.show()
