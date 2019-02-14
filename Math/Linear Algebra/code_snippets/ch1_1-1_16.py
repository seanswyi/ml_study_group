'''
An Introduction to Linear Algebra (4e) - Gilbert Strang

Chapter 1
Problem Set 1-1
#16
'''

import matplotlib.pyplot as plt


# v
plt.quiver(0, 0, 3, 1, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}$')

# w
plt.quiver(0, 0, 1, 3, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w}$')

# -v
plt.quiver(0, 0, -3, -1, color='C2', angles='xy', scale_units='xy', scale=1, label=r'$\vec{-v}$')

# 2w
plt.quiver(0, 0, 2, 6, color='C3', angles='xy', scale_units='xy', scale=1, label=r'$\vec{2w}$')

# (1/2)v + (1/2)w
plt.plot(2, 2, 'C4o', label=r'$\vec{u}$')

# -v + 2w
plt.plot(-1, 5, 'C5o', label=r'$-\vec{v} + 2\vec{w}$')

# black line
plt.plot([-4, 8], [8, -4], 'k--')

# Dotted lines.
# v
plt.plot([-1, 2], [5, 6], 'C0--')
plt.plot([0.5, 2], [1.5, 2], 'C0--')

# w
plt.plot([-3, -1], [-1, 5], 'C1--')
plt.plot([1.5, 2], [0.5, 2], 'C1--')

# Miscellaneous.
plt.xlim(-4, 9)
plt.ylim(-4, 9)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel(r'$x$', fontsize='large')
plt.ylabel(r'$y$', fontsize='large')
plt.grid()
plt.legend()
plt.show()