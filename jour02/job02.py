class Livre:
    def __init__(self,titre,nb_page):
        self._titre = titre
        self._nb_page = nb_page

    def _gettitre(self):
        return self._titre
    
    def _settitre(self, nouveau_titre):
        self._titre = nouveau_titre

    def _getnb_page(self):
        return self._nb_page
    
    def _setnb_page(self,nouveau_nb_page):
        if nouveau_nb_page < 0:
            print("le nouveau nombre de page doit être un entier positif")

    livre = property(_getnb_page,_setnb_page)


h1 = Livre("Harry Potter",500)
print("Le livre est",h1._titre,"et il fait:",h1._nb_page,"pages")
h1.livre = -4


