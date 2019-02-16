'''
An Introduction to Linear Algebra (4e) - Gilbert Strang

Chapter 1
Problem Set 1-1
#20
'''

import matplotlib.pyplot as plt


# v
plt.quiver(0, 0, 3, 1, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}$')

# w
plt.quiver(0, 0, 1, 3, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w}$')

# u
plt.quiver(0, 0, 2.5, 3.5, color='C2', angles='xy', scale_units='xy', scale=1, label=r'$\vec{u}$')

# Dotted lines.
plt.plot([1, 2.5], [3, 3.5], 'k--')
plt.plot([2.5, 3], [3.5, 1], 'k--')
plt.plot([1, 3], [3, 1], 'k--')

# (1/3)u + (1/3)v + (1/3)w
plt.plot(2.15, 2.6, 'ro', label=r'$\frac{1}{3}\vec{u} + \frac{1}{3}\vec{v} + \frac{1}{3}\vec{w}$')

# Addition dotted lines.
plt.plot([1, 2.15], [0.333, 2.6], 'C0--')
plt.plot([0.333, 2.15], [1, 2.6], 'C1--')
plt.plot([0.833, 2.15], [1.167, 2.6], 'C2--')

# Miscellaneous.
plt.xlim(-1, 6)
plt.ylim(-1, 6)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel(r'$x$', fontsize='large')
plt.ylabel(r'$y$', fontsize='large')
plt.grid()
plt.legend()
plt.show()