'''
An Introduction to Linear Algebra (4e) - Gilbert Strang

Chapter 1
Problem Set 1-1
#7
'''

import matplotlib.pyplot as plt


# c = 0, d = 0
plt.quiver(0, 0, 0, 0, color='C0', angles='xy', scale_units='xy', scale=1, label=r'$c = 0,\ d = 0$')

# c = 0, d = 1
plt.quiver(0, 0, 0, 1, color='C1', angles='xy', scale_units='xy', scale=1, label=r'$c = 0,\ d = 1$')

# c = 0, d = 2
plt.quiver(0, 0, 0, 2, color='C2', angles='xy', scale_units='xy', scale=1, label=r'$c = 0,\ d = 2$')

# c = 1, d = 0
plt.quiver(0, 0, 2, 1, color='C3', angles='xy', scale_units='xy', scale=1, label=r'$c = 1,\ d = 0$')

# c = 1, d = 1
plt.quiver(0, 0, 2, 2, color='C4', angles='xy', scale_units='xy', scale=1, label=r'$c = 1,\ d = 1$')

# c = 1, d = 2
plt.quiver(0, 0, 2, 3, color='C5', angles='xy', scale_units='xy', scale=1, label=r'$c = 1,\ d = 2$')

# c = 2, d = 0
plt.quiver(0, 0, 4, 2, color='C6', angles='xy', scale_units='xy', scale=1, label=r'$c = 2,\ d = 0$')

# c = 2, d = 1
plt.quiver(0, 0, 4, 3, color='C7', angles='xy', scale_units='xy', scale=1, label=r'$c = 2,\ d = 1$')

# c = 2, d = 2
plt.quiver(0, 0, 4, 6, color='C8', angles='xy', scale_units='xy', scale=1, label=r'$c = 2,\ d = 2$')

# Miscellaneous.
plt.xlim(-1, 8)
plt.ylim(-1, 8)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel(r'$x$', fontsize='large')
plt.ylabel(r'$y$', fontsize='large')
plt.grid()
plt.legend()
plt.show()