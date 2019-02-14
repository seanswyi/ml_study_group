'''
An Introduction to Linear Algebra (4e) - Gilbert Strang

Chapter 1
Problem Set 1-1
#15
'''

import matplotlib.pyplot as plt


# v
plt.quiver(0, 0, 3, 1, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}$')

# w
plt.quiver(0, 0, 1, 3, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w}$')

# (1/2)v + (1/2)w
plt.plot(2, 2, 'C2o', label=r'$\frac{1}{2}\vec{v} + \frac{1}{2}\vec{w}$')

# (1/4)v + (1/4)w
plt.plot(1, 1, 'C3o', label=r'$\frac{1}{4}\vec{v} + \frac{1}{4}\vec{w}$')

# (3/4)v + (1/4)w
plt.plot(2.5, 1.5, 'C4o', label=r'$\frac{3}{4}\vec{v} + \frac{1}{4}\vec{w}$')

# v + w
plt.plot(4, 4, 'C5o', label=r'$\vec{v} + \vec{w}$')

# Dotted lines.
# v
plt.plot([0.25, 2.5], [0.75, 1.5], 'C0--')
plt.plot([0.5, 2], [1.5, 2], 'C0--')
plt.plot([1, 4], [3, 4], 'C0--')

# w
plt.plot([0.75, 1], [0.25, 1], 'C1--')
plt.plot([1.5, 2], [0.5, 2], 'C1--')
plt.plot([2.25, 2.5], [0.75, 1.5], 'C1--')
plt.plot([3, 4], [1, 4], 'C1--')

# Miscellaneous.
plt.xlim(-1, 7)
plt.ylim(-1, 7)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel(r'$x$', fontsize='large')
plt.ylabel(r'$y$', fontsize='large')
plt.grid()
plt.legend()
plt.show()