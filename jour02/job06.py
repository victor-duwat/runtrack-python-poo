class Plat:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix
        self.statut = "en cours"


class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = []
        self.__statut_commande = "en cours"

    def ajouter_plat(self, plat):
        plat.statut = self.__statut_commande
        self.__plats_commandes.append(plat)

    def annuler_commande(self):
        self.__statut_commande = "annulée"
        for plat in self.__plats_commandes:
            plat.statut = self.__statut_commande

    def calculer_total(self):
        total = 0
        for plat in self.__plats_commandes:
            total += plat.prix
        return total

    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande}")
        for plat in self.__plats_commandes:
            print(f"{plat.nom}: {plat.prix} €")
        print(f"Total à payer: {self.calculer_total()} €")

    def calculer_tva(self, taux_tva=0.20):
        return self.calculer_total() * taux_tva

plat1 = Plat("Pizza", 10.99)
plat2 = Plat("Pâtes", 7.50)

commande1 = Commande(1)
commande1.ajouter_plat(plat1)
commande1.ajouter_plat(plat2)
commande1.afficher_commande()

commande1.annuler_commande()
commande1.afficher_commande()
print(f"TVA à payer: {commande1.calculer_tva()} €")
