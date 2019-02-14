'''
An Introduction to Linear Algebra (4e) - Gilbert Strang

Chapter 1
Problem Set 1-1
#8
'''

import matplotlib.pyplot as plt


# v
plt.quiver(0, 0, 4, 2, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}$')

# w
plt.quiver(0, 0, -1, 2, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w}$')

# -w
plt.quiver(0, 0, 1, -2, color='C2', angles='xy', scale_units='xy', scale=1, label=r'$\vec{-w}$')

# v + w
plt.quiver(0, 0, 3, 4, color='C3', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v} + \vec{w}$')

# v - w
plt.quiver(0, 0, 5, 0, color='C4', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v} - \vec{w}$')

# Dotted lines.
plt.plot([-1, 3], [2, 4], 'C0--')
plt.plot([3, 4], [4, 2], 'C1--')
plt.plot([1, 5], [-2, 0], 'C0--')
plt.plot([4, 5], [2, 0], 'C2--')

# Miscellaneous.
plt.xlim(-4, 7)
plt.ylim(-4, 7)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel(r'$x$', fontsize='large')
plt.ylabel(r'$y$', fontsize='large')
plt.grid()
plt.legend()
plt.show()