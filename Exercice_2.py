import matplotlib.pyplot as plt
import numpy as np

class Curve:
    def __init__(self, start=0, stop=1, nbr_points=5432):
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points

    def __f(self, x):
        return x**3

    def plot_curve(self):
        x = np.linspace(self.start, self.stop, 100)
        y = self.__f(x)
        plt.plot(x, y)

        plt.plot([0, 1], [0, 0], 'k-') # bottom side
        plt.plot([0, 0], [0, 1], 'k-') # left side
        plt.plot([1, 1], [0, 1], 'k-') # top side
        plt.plot([0, 1], [1, 1], 'k-') # right side

        plt.xlim(self.start, self.stop)
        plt.ylim(0, 1)

        plt.show()

    def is_above_curve(self, x, y):
        return y > self.__f(x)

    def generate_points(self):
        x = np.linspace(self.start, self.stop, self.nbr_points)
        y = np.random.uniform(0, 1, self.nbr_points)

        above_curve = []
        below_curve = []

        for i in range(self.nbr_points):
            if self.is_above_curve(x[i], y[i]):
                above_curve.append([x[i], y[i]])
                plt.plot(x[i], y[i], 'bo') # blue point
            else:
                below_curve.append([x[i], y[i]])
                plt.plot(x[i], y[i], 'go') # green point

        plt.show()

        return above_curve, below_curve

    def calculate_areas(self):
        above_curve, below_curve = self.generate_points()

        area_above_curve = 0
        for point in above_curve:
            area_above_curve += 0.5 * (1 - point[1]) * (point[0] - self.start)

        area_below_curve = 0
        for point in below_curve:
            area_below_curve += 0.5 * (1 - point[1]) * (point[0] - self.start)

        return area_above_curve, area_below_curve


# créer une instance de la classe Curve
#curve = Curve()

# tracer la courbe
#curve.plot_curve()

# générer des points aléatoires
#above_curve, below_curve = curve.generate_points()

# calculer les surfaces en bleu et en vert
#area_above_curve, area_below_curve = curve.calculate_areas()

# afficher les résultats
#print("Surface en bleu :", area_above_curve)
#print("Surface en vert :", area_below_curve)