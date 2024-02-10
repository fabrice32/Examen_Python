# créer une instance de la classe Curve
from Exercice_2 import Curve

curve = Curve()

# tracer la courbe
#curve.plot_curve(

# générer des points aléatoires
above_curve, below_curve = curve.generate_points()

# calculer les surfaces en bleu et en vert
area_above_curve, area_below_curve = curve.calculate_areas()

# afficher les résultats
print("Surface en bleu :", area_above_curve)
print("Surface en vert :", area_below_curve)