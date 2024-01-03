class Student:

    def __init__(self,prenom,nom,num_etudiant,nombre_de_credits):
        self._nom = nom
        self._prenom = prenom
        self._num_etudiant = num_etudiant
        self._nombre_de_credits = nombre_de_credits
        self._level =("")

    def add_credits(self,x):
        if x >0:
            self._nombre_de_credits+=x
            print(x,"crédits ont été ajouté à votre compte")
        else:
            print("venez ajouter un nombre positif de crédits")

    def studentEval(self):
        if self._nombre_de_credits >=90:
            self._level=("Excellent")
        elif self._nombre_de_credits >=80:
            self._level=("Très bien")
        elif self._nombre_de_credits >=70:
            self._level=("Bien")
        elif self._nombre_de_credits >=60:
            self._level=("Passable")
        elif self._nombre_de_credits <60:
            self._level=("Insuffisant")
        return self._level
    
    def StudentInfo(self):
        print("Nom=",etudiant._prenom)
        print("Prénom =",etudiant._nom)
        print("id=",etudiant._num_etudiant)
        print("Niveau=",etudiant.studentEval())
            


etudiant = Student("John","Doe",145,0)

print("le nombre de credits de",etudiant._prenom,etudiant._nom,"est de",etudiant._nombre_de_credits)

etudiant.add_credits(10)
etudiant.add_credits(10)
etudiant.add_credits(60)

print("le nombre de credits de",etudiant._prenom,etudiant._nom,"est de",etudiant._nombre_de_credits)

etudiant.StudentInfo()
