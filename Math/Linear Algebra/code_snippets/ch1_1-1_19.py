'''
An Introduction to Linear Algebra (4e) - Gilbert Strang

Chapter 1
Problem Set 1-1
#19
'''

import matplotlib.pyplot as plt


# v
plt.quiver(0, 0, 3, 1, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}$')

# w
plt.quiver(0, 0, 1, 3, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w}$')

# Draw polygon.
polygon = plt.Polygon([[0, 0], [2, 6], [6, 6], [6, 2], [0, 0]], color='C2', zorder=0, label=r'$c\vec{v} + d\vec{w}$')
plt.gca().add_patch(polygon)

# Miscellaneous.
plt.xlim(-1, 6)
plt.ylim(-1, 6)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel(r'$x$', fontsize='large')
plt.ylabel(r'$y$', fontsize='large')
plt.grid()
plt.legend(loc='upper left')
plt.show()