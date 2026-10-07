import matplotlib.pyplot as plt
import math

G = 6.674e-11
M, R = 5.972e24, 6.371e6
m = 1

h = 80000
u = 8000

t = 0
x, y = R, 0
x_vals, y_vals = [], []
dt = 0.01
while (t < 2*math.pi):
    x_vals.append(x)
    y_vals.append(y)

    x = R * math.cos(t)
    y = R * math.sin(t)

    t += dt
plt.plot(x_vals, y_vals, color="#0000ff")
plt.plot([0, 0], [R, R + h], color="#000000")
del x_vals, y_vals, x, y, t, dt

t = 0
T = 5000
x, y, vx, vy = 0, R + h, u, 0
F = G * M * m / (x**2 + y**2)
Fx, Fy = -F * x / (x**2 + y**2)**0.5, -F * y / (x**2 + y**2)**0.5

dt = 0.1

t_vals, x_vals, y_vals = [], [], []
while (t < T):
    t_vals.append(t)
    x_vals.append(x)
    y_vals.append(y)

    x += vx * dt
    y += vy * dt

    vx += (Fx / m) * dt
    vy += (Fy / m) * dt

    F = G * M * m / (x**2 + y**2)
    Fx, Fy = -F * x / (x**2 + y**2)**0.5, -F * y / (x**2 + y**2)**0.5

    t += dt

plt.plot(x_vals, y_vals)
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.grid(True)
plt.axis([-2*R, 2*R, -2*R, 2*R])
plt.axis('equal')
plt.show()