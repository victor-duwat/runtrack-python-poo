class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print("Statistiques de",self.nom,"N°",self.numero,self.position)
        print("Buts marqués:", self.buts_marques)
        print("Passes décisives:",self.passes_decisives)
        print("Cartons jaunes:", self.cartons_jaunes)
        print("Cartons rouges:", self.cartons_rouges)

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, nouveau_joueur):
        self.joueurs.append(nouveau_joueur)

    def afficherStatistiquesJoueurs(self):
        print("Statistiques des joueurs de l'équipe",self.nom,":")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, joueur, action):
        if action == "but":
            joueur.marquerUnBut()
        elif action == "passe":
            joueur.effectuerUnePasseDecisive()
        elif action == "carton_jaune":
            joueur.recevoirUnCartonJaune()
        elif action == "carton_rouge":
            joueur.recevoirUnCartonRouge()

joueur1 = Joueur("Messi", 10, "Attaquant")
joueur2 = Joueur("Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Iniesta", 8, "Milieu")
joueur4 = Joueur("Sergio Ramos", 4, "Défenseur")

equipe1 = Equipe("Barcelona")
equipe2 = Equipe("Real Madrid")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)

equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur4)

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur(joueur1, "but")
equipe1.mettreAJourStatistiquesJoueur(joueur3, "passe")

equipe2.mettreAJourStatistiquesJoueur(joueur2, "but")
equipe2.mettreAJourStatistiquesJoueur(joueur4, "carton_jaune")

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
