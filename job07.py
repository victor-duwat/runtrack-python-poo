class Personnage :
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def gauche(self):
        self.x-=1
        print("le personnage se déplace sur la gauche")
    
    def droite(self):
        self.x+=1
        print("le personnage se déplace sur la droite")
    def haut(self):
        self.y+=1
        print("le personnage se déplace vers le haut")
    def bas(self):
        self.y-=1
        print("le personnage se déplace vers le bas")
    def position(self):
        print("la position du personnage est en x de:",self.x,"et ça position en y est de:",self.y)

personnage=Personnage(6,4)
personnage.gauche()
personnage.gauche()
personnage.bas()
personnage.position()
personnage.droite()
personnage.haut()
personnage.position()