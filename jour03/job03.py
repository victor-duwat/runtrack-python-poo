class Tache:
    def __init__(self, titre, description, statut):
        self._titre = titre
        self._description = description
        self._statut = statut

    def _get_titre(self):
        return self._titre
    
    def _get_description(self):
        return self._description
    
    def _get_statut(self):
        return self._statut

    def marquerCommeFinie(self):
        self._statut = True

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, nouvelle_tache):
        self.taches.append(nouvelle_tache)

    def supprimerTache(self, tache_a_supprimer):
        self.taches.remove(tache_a_supprimer)
        print("la tache",self.taches,"à été supprimer")

    def marquerCommeFinie(self, tache_a_finir):
        tache_a_finir.marquerCommeFinie()

    def recupererListeTaches(self):
        return self.taches
    
    def afficherListe(self):
        for tache in self.taches:
            statut_affichage = "finis" if tache._get_statut() else "pas finis"
            print("Tâche:", tache._get_titre(), "Description:", tache._get_description(), "Statut:", statut_affichage)

tache1 = Tache("vaisselle", "ranger le lave-vaisselle", False)
tache2 = Tache("courses", "acheter des fruits", True)

liste_de_taches = ListeDeTaches()
liste_de_taches.ajouterTache(tache1)
liste_de_taches.ajouterTache(tache2)

liste_de_taches.afficherListe()

liste_de_taches.marquerCommeFinie(tache1)

liste_de_taches.afficherListe()
