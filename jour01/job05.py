class Point :
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y 
    
    def afficherLesPoints(self):
        print("la coordonné du point en X et Y est:",self.x,self.y)
    
    def afficheX(self):
        print("la coordoné du point en X est: ",self.x)

    def afficheY(self):
        print("la coordoné du point en Y est: ",self.y)

    def changerX(self,x):
        self.x=x

    def changerY(self,y):
        self.y=y

personnage=Point(7,6)
personnage.afficheX()
personnage.afficheY()
personnage.changerX(2)
personnage.changerY(3)
personnage.afficherLesPoints()