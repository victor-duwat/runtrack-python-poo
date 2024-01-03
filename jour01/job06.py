class Animal:
    def __init__(self,age,nom):
        self.age = age
        self.nom = nom

    def nommer(self):
        print("l'animal a:",self.age,"ans et s'apelle",self.nom)

    def vieillir(self):
        self.age+=1
        print("l'animal a maintenant:",self.age,"ans")


animal=Animal(0,"Luna")
animal.nommer()
animal.vieillir()