from math import *
class Cercle:
    def __init__(self,r,) -> None:
        self.r = r
    
    def circonférence(self):
        p=2*pi*self.r
        print("la circonférence du cercle est de: ",p,"cm")
    
    def aire(self):
        a=pi*self.r*self.r
        print("l'aire du cercle est de:",a,"cm^2")

    def diamètre(self):
        d=self.r*2
        print("le diamètre du cercle est de:",d,"cm")
    
    def afficherInfos(self):
        d=self.r*2
        p=2*pi*self.r
        a=pi*self.r*self.r
        print("le cercle à un rayon de",self.r,"cm")
        print("le cercle à une circonférence de:",p,"cm")
        print("le cercle à une aire de:",a,"cm^2")
        print("le cercle à un diamètre de: ",d,"cm")


cercle1=Cercle(7)
cercle2=Cercle(4)

print("voici les informations du cercle 1:")
cercle1.afficherInfos()

print("voici les informations du cercle 2:")
cercle2.afficherInfos()
