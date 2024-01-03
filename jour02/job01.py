class Rectangle:

    def __init__(self,longueur,largeur):
        self._longueur = longueur
        self._largeur = largeur

    def _getlargeur(self):
        return self._largeur
    
    def _setlargeur(self,nouvel_largeur):
        self._largeur = nouvel_largeur

    
    largeur = property(_getlargeur,_setlargeur)

    def _getlongueur(self):
        return self._longueur
    
    def _setlongueur(self, nouvel_longueur):
        self._longueur = nouvel_longueur

    longueur = property(_getlongueur,_setlongueur)
    
rect = Rectangle(10,5)
print("la longueur du rectangle est de: ",rect.longueur,"et la largeur de",rect.largeur)
rect.longueur = 3
rect.largeur = 8
print("la nouvelle longueur du rectangle est de:",rect.longueur,"et la nouvelle largeur de:",rect.largeur)