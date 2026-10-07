import matplotlib.pyplot as plt
import math

G = 6.674e-11 # gravitational constant
M, R = 5.972e24, 6.371e6 # mass and radius of Earth
m = 1 # mass of cannonball

h = 0 # height of mountain
u = 10000 # initial speed of cannonball

# drawing the Earth and the Mountain
t = 0
x, y = R, 0
x_vals, y_vals = [], []
dt = 0.01
tol = 100
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
T = 20000
x, y, vx, vy = 0, R + h, u, 0 # initial position and velocity of cannonball
F = G * M * m / (x**2 + y**2)
Fx, Fy = -F * x / (x**2 + y**2)**0.5, -F * y / (x**2 + y**2)**0.5

dt = 0.02

t_vals, x_vals, y_vals = [], [], []
while ((abs(x - 0) > tol or abs(y - (R + h)) > tol) and t < T or len(t_vals) == 0):
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

plt.plot(x_vals, y_vals, ls='--', color="#00e1ff")
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.grid(True)
plt.axis([-2*R, 2*R, -2*R, 2*R])
plt.axis('equal')
plt.show()
