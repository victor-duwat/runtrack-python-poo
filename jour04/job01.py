class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("Âge de la personne :", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        super().__init__(age)
        self._matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


personne1 = Personne()
personne1.afficherAge()
personne1.bonjour()


eleve1 = Eleve()
eleve1.afficherAge()  

professeur1 = Professeur(matiereEnseignee="Mathématiques")
professeur1.enseigner()