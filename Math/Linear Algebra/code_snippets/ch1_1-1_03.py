'''
An Introduction to Linear Algebra (4e) - Gilbert Strang

Chapter 1
Problem Set 1-1
#3
'''

import matplotlib.pyplot as plt


# v
plt.quiver(0, 0, 3, 3, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v}$')

# w
plt.quiver(0, 0, 2, -2, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w}$')

# Miscellaneous.
plt.xlim(-3, 5)
plt.ylim(-3, 5)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel(r'$x$', fontsize='large')
plt.ylabel(r'$y$', fontsize='large')
plt.grid()
plt.legend()
plt.show()