class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, ennemi):
        degats = 10
        ennemi.subir_degats(degats)

    def subir_degats(self, degats):
        self.vie -= degats
        if self.vie < 0:
            self.vie = 0

    def get_en_vie(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisir_niveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1, 2, 3) : "))

    def lancement_jeu(self):
        self.choisir_niveau()

        vie_joueur = 130 + 10 * self.niveau
        vie_ennemi = 100 + 25 * self.niveau

        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        while joueur.get_en_vie() and ennemi.get_en_vie():
            joueur.attaquer(ennemi)
            if ennemi.get_en_vie():
                ennemi.attaquer(joueur)

        self.afficher_resultat(joueur, ennemi)

    def afficher_resultat(self, joueur, ennemi):
        if joueur.get_en_vie():
            print(joueur.nom, "a gagné !")
        else:
            print(ennemi.nom, "a gagné !")  

jeu = Jeu()
jeu.lancement_jeu()