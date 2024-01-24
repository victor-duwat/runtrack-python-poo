class Rectangle:
    def __init__(self, longueur=3, largeur=7):
        self.longueur = longueur
        self.largeur = largeur

    def perimetre(self):
        return (self.longueur + self.largeur) * 2

    def surface(self):
        return self.longueur * self.largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur=3, largeur=7, hauteur=6):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        surface_rectangle = super().surface()
        return surface_rectangle * self.hauteur


rectangle = Rectangle(2, 6)
print("Périmètre du rectangle:", rectangle.perimetre())
print("Surface du rectangle:", rectangle.surface())

parallelepipede = Parallelepipede(2,6,8)
print("Volume du parallelepipede:", parallelepipede.volume())