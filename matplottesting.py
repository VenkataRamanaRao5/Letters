import matplotlib.pyplot as plt
import numpy as np

limit = 2.5

a, b = 0.4, 1
c = 0.4

parameters = [
    [0.1, -15],
    [0.2, -11],
    [0.25, -7],
    [-0.05, -3],
    [1.05, 1],
    [0.8, 5],
    [-0.25, 9]
]

angles = np.linspace(0, 2*np.pi, 1000)
points = 0
for parameter in parameters:
    points += parameter[0] * np.exp(1j * parameter[1] * angles)
#points = 0.9 * np.exp(1j * angles) + 0.4 * np.exp(1j * -3 * angles) + 0.3 * np.exp(1j * 5 * angles) + 0.4 * np.exp(1j * -7 * angles) + 0.1 * np.exp(1j * 9 * angles)

fig, ((axs, axs2), (axs3, _)) = plt.subplots(2, 2)

axs.set_aspect('equal')
axs.set_xlim(-limit, limit)
axs.set_ylim(-limit, limit)
axs.plot([0, 0], [limit, -limit], color = 'blue')
axs.plot([limit, -limit], [0, 0], color = 'blue')
axs.plot(points.real, points.imag, color = 'orange')

# axs2.set_aspect('equal')
# axs2.plot([0, 8], [0, 0], color = 'blue')
axs2.plot(angles, abs(points), color = 'red')

# axs3.set_aspect('equal')
# axs3.plot([0, 8], [0, 0], color = 'blue')
axs3.plot(angles, (np.angle(points) + np.pi * 2) % (2 * np.pi), color = 'red')
plt.show()

# four point

theta = angles - c * np.sin(4 * angles)
r = ((np.cos(4 * angles) + 1) * 0.5) ** 1.2 * (b - a) + a
points = 1 * np.exp(1j * angles) + 0.45 * np.exp(1j * -3 * angles)

#rangloi

parameters = [
    [0.1, -15],
    [0.2, -11],
    [0.2, -7],
    [-0.1, -3],
    [1.1, 1],
    [0.75, 5],
    [-0.3, 9]
]

parameters = [
    [0.1, -15],
    [0.2, -11],
    [0.25, -7],
    [-0.05, -3],
    [1.05, 1],
    [0.8, 5],
    [-0.25, 9]
]


theta = (angles + 2.25 * np.sin(angles) - 3.5 * np.sin(2 * angles)) / 4 
r = (np.cos(angles) + np.cos(3 * angles)) * 0.25 * (b - a) + a