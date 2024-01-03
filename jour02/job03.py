class Livre:
    def __init__(self,titre,nb_page,disponible):
        self._titre = titre
        self._nb_page = nb_page
        self._disponible = disponible
        self._emprun = False

    def _gettitre(self):
        return self._titre
    
    def _settitre(self, nouveau_titre):
        self._titre = nouveau_titre

    def _getnb_page(self):
        return self._nb_page
    
    def _setnb_page(self,nouveau_nb_page):
        if nouveau_nb_page < 0:
            print("le nouveau nombre de page doit être un entier positif")

    def verification (self):
        if self._disponible == True :
            return self._disponible
        else:
            self._disponible = False

    def emprunter (self):
        if self.verification() == True:
            print("vous empruntez le livre")
            self._disponible = False
        else:
            print("vous ne pouvez pas emprunter le livre")
        self._emprun=True

    def rendre (self):
        if self._emprun == True:
            print("vous rendez votre livre à rendre")
            self._disponible == False
        else:
            print("Vous n'avez pas de livre emprunter")


            

            

    livre = property(_getnb_page,_setnb_page)

h1 = Livre("Harry Potter",500,True)
print("Le livre est",h1._titre,"et il fait:",h1._nb_page,"pages")
h1.emprunter()
h1.emprunter()

print('\n')

h1 = Livre("Seigneur des anneaux",600,False)
print("Le livre est",h1._titre,"et il fait:",h1._nb_page,"pages")
h1.emprunter()

print('\n')

h1 = Livre("Star wars",500,True)
print("Le livre est",h1._titre,"et il fait:",h1._nb_page,"pages")
h1.emprunter()
h1.rendre()