class Voiture:

    def __init__(self,marque,modèle,année,kilométrage,en_marche,reservoir):
        self._marque = marque
        self._modèle = modèle 
        self._année = année
        self._kilométrage = kilométrage
        self._en_marche = en_marche
        self._en_marche = False
        self._reservoir = reservoir
        self._reservoir = 50

        def demarrer(self):

            if verifier_plein()>=5:
                self._en_marche = True
            return self._en_marche

        def arreter(self):

            self._en_marche = False
            return self._en_marche

        def verifier_plein(self):
            
            return self._reservoir
        


