class Operation :
    
    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def affiche_nombre(self):
        print("le nombre1 est:",self.nombre1)
        print("le nombre 2 est:",self.nombre2)

affiche = Operation(12,3)
affiche.affiche_nombre()
