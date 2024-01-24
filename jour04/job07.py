import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
        random.shuffle(paquet)
        return paquet

    def calculer_total(self, main):
        total = 0
        as_present = False

        for carte in main:
            if carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            elif carte.valeur == 'As':
                as_present = True
                total += 1
            else:
                total += int(carte.valeur)

        if as_present and total + 10 <= 21:
            total += 10

        return total

    def afficher_main(self, main):
        for carte in main:
            print(f"{carte.valeur} de {carte.couleur}")

    def jouer_partie(self):
        joueur_main = [self.paquet.pop(), self.paquet.pop()]
        croupier_main = [self.paquet.pop(), self.paquet.pop()]

        print("Main du joueur:")
        self.afficher_main(joueur_main)

        while True:
            choix = input("Voulez-vous prendre une carte supplémentaire ? (o/n): ").lower()
            if choix == 'o':
                joueur_main.append(self.paquet.pop())
                print("Main du joueur:")
                self.afficher_main(joueur_main)

                total_joueur = self.calculer_total(joueur_main)
                if total_joueur > 21:
                    print("Vous avez dépassé 21, vous avez perdu !")
                    return
            elif choix == 'n':
                break

        while self.calculer_total(croupier_main) < 17:
            croupier_main.append(self.paquet.pop())

        print("\nMain du croupier:")
        self.afficher_main(croupier_main)

        total_joueur = self.calculer_total(joueur_main)
        total_croupier = self.calculer_total(croupier_main)

        print(f"\nTotal du joueur: {total_joueur}")
        print(f"Total du croupier: {total_croupier}")

        if total_joueur > 21 or (total_croupier <= 21 and total_croupier >= total_joueur):
            print("Le croupier gagne.")
        else:
            print("Le joueur gagne.")

jeu_blackjack = Jeu()
jeu_blackjack.jouer_partie()