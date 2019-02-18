import matplotlib.pyplot as plt

# v
plt.quiver(0, 0, 6, 4, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}$')

# w
plt.quiver(0, 0, 1, 5, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w}$')

# perpendicular line
plt.plot([1, 3], [5, 2], 'k--')

# comp_vw
plt.plot([0, 3,], [0, 2], 'r-', label=r'${comp}_{\vec{v}}{\vec{w}}$')

plt.xlim(-1, 8)
plt.ylim(-1, 8)
plt.legend()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel(r'$x$', fontsize='large')
plt.ylabel(r'$y$', fontsize='large')
plt.grid()
plt.show()