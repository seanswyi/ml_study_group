'''
An Introduction to Linear Algebra (4e) - Gilbert Strang

Chapter 1
Problem Set 1-1
#2
'''

import matplotlib.pyplot as plt


# v
plt.quiver(0, 0, 4, 1, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}$')

# w
plt.quiver(0, 0, -2, 2, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w}$')

# -w
plt.quiver(0, 0, 2, -2, color='C2', angles='xy', scale_units='xy', scale=1, label=r'$\vec{-w}$')

# v + w
plt.quiver(0, 0, 2, 3, color='C3', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v} + \vec{w}$')

# v - w
plt.quiver(0, 0, 6, -1, color='C4', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v} - \vec{w}$')

# Dotted lines.
plt.plot([-2, 2], [2, 3], 'C0--')
plt.plot([2, 4], [3, 1], 'C1--')
plt.plot([2, 6], [-2, -1], 'C0--')
plt.plot([4, 6], [1, -1], 'C2--')

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