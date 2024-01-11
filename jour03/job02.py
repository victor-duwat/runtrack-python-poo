class CompteBancaire:

    def __init__(self,num_compte,nom,prenom,solde,decouvert):

        self._num_compte = num_compte
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._decouvert = decouvert
        self._decouvert = True

    def _get_solde(self):
        return self._solde

    def afficherSolde(self):
        print("votre compte est de:",self._solde)

    def versement(self,x):
        self._solde += x
        print("un versement de:",x,"à été ajouter à votre compte, votre compte est maintenant de:",self._solde)

    def retrait(self,x):
        self._solde -= x
        print("un retrait de:",x,"à été enlever à votre compte, votre compte est maintenant de:",self._solde)

    def afficher(self):
        print("Bonjour monsieur,",self._nom,self._prenom,"votre numéro de compte est le ",self._num_compte,"et il contient",self._solde,"euros")


    def agios(self):
        x=20
        if self._decouvert == True:
            self._solde -= x
            print("vous avez subis un agios de:",x,"euros")
    
    def virement(self,CompteBancaire,x):
        compte = CompteBancaire._get_solde()
        if compte < x:
            print("vous n'avez pas assez d'argent pour faire le virement")
        else:
            
            self._solde += x
            print("le virement à été effectuer, votre solde est de:",self._solde)


compte1 = CompteBancaire(10,"Duwat","Victor",100,False)

compte1.afficher()

compte1.versement(50)

compte1.retrait(20)
    
compte1.afficher()

compte2 = CompteBancaire(9,"John","Cena",200,False)

compte1.afficherSolde()

compte1.virement(compte2,50)

