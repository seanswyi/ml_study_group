'''
An Introduction to Linear Algebra (4e) - Gilbert Strang

Chapter 1
Problem Set 1-1
#17
'''

import matplotlib.pyplot as plt


# v
plt.quiver(0, 0, 3, 1, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}$')

# w
plt.quiver(0, 0, 1, 3, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w}$')

# (1/3)v + (1/3)w
plt.plot(1.333, 1.333, 'C4o', label=r'$\frac{1}{3}\vec{v} + \frac{1}{3}\vec{w}$')

# (2/3)v + (2/3)w
plt.plot(2.666, 2.666, 'C5o', label=r'$\frac{2}{3}\vec{v} + \frac{2}{3}\vec{w}$')

# black line
plt.plot([0, 6], [0, 6], 'k--')

# Dotted lines.
# v
plt.plot([0.333, 1.333], [1, 1.333], 'C0--')
plt.plot([0.666, 2.666], [2, 2.666], 'C0--')

# w
plt.plot([1, 1.333], [0.333, 1.333], 'C1--')
plt.plot([2, 2.666], [0.666, 2.666], 'C1--')

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