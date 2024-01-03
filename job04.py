class Personne :
    
    def __init__(self,nom,prenom):
        self.nom = nom
        self.prenom = prenom
    def SePresenter(self):
        print("Je suis",self.prenom,self.nom)

presenter1 = Personne("Duwat","Victor")
presenter1.SePresenter()

presenter2 = Personne("Macron","Emmanuel")
presenter2.SePresenter()