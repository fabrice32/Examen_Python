import matplotlib.pyplot as plt
import numpy as np

# Fonction definissant la courbe
def f(x):
    return x**3

# Tracer la courbe
x = np.linspace(0, 1, 100)
y = f(x)
plt.plot(x, y)

# Tracer le carré
plt.plot([0, 1], [0, 0], 'k-') # bottom side
plt.plot([0, 0], [0, 1], 'k-') # left side
plt.plot([1, 1], [0, 1], 'k-') # top side
plt.plot([0, 1], [1, 1], 'k-') # right side

# Fixer les limites du graphique
plt.xlim(0, 1)
plt.ylim(0, 1)

# Affichage du graphique
plt.show()