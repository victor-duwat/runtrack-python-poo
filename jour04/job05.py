import math

class Forme:
    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius**2

cercle = Cercle(radius=4)

resultat_aire_cercle = cercle.aire()

print("Aire du cercle:", resultat_aire_cercle)