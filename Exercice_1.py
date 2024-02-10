import matplotlib.pyplot as plt
import numpy as np

# Function defining the curve
def f(x):
    return x**3

# Plotting the curve
x = np.linspace(0, 1, 100)
y = f(x)
plt.plot(x, y)

# Plotting the square
plt.plot([0, 1], [0, 0], 'k-') # bottom side
plt.plot([0, 0], [0, 1], 'k-') # left side
plt.plot([1, 1], [0, 1], 'k-') # top side
plt.plot([0, 1], [1, 1], 'k-') # right side

# Setting the limits
plt.xlim(0, 1)
plt.ylim(0, 1)

# Displaying the plot
plt.show()