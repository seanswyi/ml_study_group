import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(0, 7)
ax.set_ylim(0, 7)
ax.set_zlim(0, 7)
ax.view_init(elev=20, azim=32)

x, y, z = np.zeros((3, 3))
u, v, w = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]])

ax.quiver(0, 0, 0, 1, 1, 0, color='C0', arrow_length_ratio=0.1, label=r'$\vec{v}$')
ax.plot([1, 0], [1, 1], 0, 'k--')
ax.plot([1, 1], [0, 1], 0, 'k--')

ax.quiver(0, 0, 0, 2, 3, 5, color='C1', arrow_length_ratio=0.1, label=r'$\vec{u}$')
ax.plot([2, 2], [0, 3], 0, 'k--')
ax.plot([0, 2], [3, 3], 0, 'k--')
ax.plot([2, 2], [3, 3], [0, 5], 'k--')

plt.legend()
ax.set_xlabel(r'$x$', fontsize='large')
ax.set_ylabel(r'$y$', fontsize='large')
ax.set_zlabel(r'$z$', fontsize='large')

plt.show()