class Ville:
    
    def __init__(self,nom,nb_habitant):
        self._nom = nom
        self._nb_habitant = nb_habitant

    def _get_nom(self):
        return self._nom
    
    def _get_nb_habitant(self):
        return self._nb_habitant
    
    def augmenter_habitant(self):
        self._nb_habitant +=1


class Personne: 
    
    def __init__(self,nom,age,ville,):
        self._nom = nom
        self._age = age 
        self._ville = ville

    def _get_nom(self):
        return self._nom
    
    def _get_age(self):
        return self._age
    
    def _get_ville(self):
        return self._ville._get_nom()



    def ajoutePopulation(self):
        self._ville.augmenter_habitant()


Paris = Ville("Paris",1000000)
Marseille = Ville("Marseille",861635)

John = Personne("John",45,Paris)
Myrtille = Personne("Myrtille",4,Paris)
Chloe = Personne("Chloe",18,Marseille)

print("Population de la vile de",Paris._nom,"est de:",Paris._nb_habitant)
print("Population de la vile de",Marseille._nom,"est de:",Marseille._nb_habitant)

John.ajoutePopulation()
Myrtille.ajoutePopulation()
Chloe.ajoutePopulation()

print("mise à jour de la ville de Paris",Paris._nb_habitant,"habitant")
print("Mise à jour de la ville de Marseille",Marseille._nb_habitant,"habitant")





