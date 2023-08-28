class Humain:
    """
    classe qui definit un humain
    """
    lieu_habitation = "Terre"
    def __init__(self, c_prenom = "toto", c_age=1):
        print("Creation d'un humain")
        # creation d'attribut
        self.prenom = c_prenom
        self._age = c_age
        
    ## les methodes
    def parler(self, message): # self = methode standard
        print("{} a dit : {} ".format(self.prenom, message)
              )
        
        
    ## methode de classe
    def  changer_planete(cls, nouvelle_planete): #cls est une methode de classe
        Humain.lieu_habitation = nouvelle_planete
    changer_planete = classmethod(changer_planete)
    
    ## methode statique
    def Definition():
        print("l'humain est classe comme etant le plus etre vivant de la chaine alimentaire....")
        
    Definition = staticmethod(Definition)
    
    ## lencapsulation 
        #poperty(getter, setter, deleter, helper)
    def _getage(self):
        try:
            return self._age
        except AttributeError:
            print("L'age nexiste pas !")
            
    def _setage(self, nouvel_age):
        if nouvel_age < 0:
            self._age = 0
        else :
            self._age = nouvel_age
    def _delage(self):
        del self._age
    age = property(_getage, _setage, _delage, "Je suis l'age de l'humain")
       
## Programme principal
h1 = Humain("Jason", 26)
h1.parler("Bonjour a tous ! : ")
h1.parler("comment allez-vous?")

## methode de classe
print()
print("Planete actuelle : {}".format(Humain.lieu_habitation))
Humain.changer_planete("Mars")
print("Planete actuelle : {}".format(Humain.lieu_habitation))


## les methode statique
print()
Humain.Definition()


## Propriete d'encapsulation

print(h1.age)
h1.age = 20
print(h1.age)
del h1.age
print(h1.age)
help(Humain.age) 