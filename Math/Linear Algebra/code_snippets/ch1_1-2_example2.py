import matplotlib.pyplot as plt

# v
plt.quiver(0, 0, 6, 4, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}$')

# w
plt.quiver(0, 0, 1, 5, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w}$', zorder=0)

# u
plt.quiver(0, 0, -2, 3, color='C2', angles='xy', scale_units='xy', scale=1, label=r'$\vec{u}$')

# comp
plt.quiver(0, 0, 3, 2, color='C3', angles='xy', scale_units='xy', scale=1, label=r'$\vec{comp}$')

# dotted lines
plt.plot([1, 3], [5, 2], 'C2--')
plt.plot([-2, 1], [3, 5], 'C3--')

plt.xlim(-4, 8)
plt.ylim(-4, 8)
plt.legend()
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel(r'$x$', fontsize='large')
plt.ylabel(r'$y$', fontsize='large')
plt.grid(True)
plt.show()