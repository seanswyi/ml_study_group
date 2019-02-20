'''
An Introduction to Linear Algebra (4e) - Gilbert Strang

Chapter 1
Problem Set 1-1
#21
'''

import matplotlib.pyplot as plt


# v - u
plt.quiver(-1, 1, 4, 0, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$\vec{v} - \vec{u}$')

# w - v
plt.quiver(3, 1, -5, -3, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$\vec{w} - \vec{v}$')

# u - w
plt.quiver(-2, -2, 1, 3, color='C2', angles='xy', scale_units='xy', scale=1, label=r'$\vec{u} - \vec{w}$')

# points
plt.plot(3, 1, 'ko')
plt.plot(-1, 1, 'ko')
plt.plot(-2, -2, 'ko')

# Miscellaneous.
plt.xlim(-5, 6)
plt.ylim(-5, 6)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel(r'$x$', fontsize='large')
plt.ylabel(r'$y$', fontsize='large')
plt.grid()
plt.legend()
plt.show()