
## Classe Mere
class Vehicule:
    def __init__(self, nom_vehicule, quantite_essence):
        self.nom =nom_vehicule
        self.essence = quantite_essence
        
    def montrer_vehicule (self):
        return self.nom
    
    def se_deplacer(self):
        print("le vehicule {} se deplace..".format(self.nom))
    
    
## Classe fille

class voiture(Vehicule):
    def __init__(self, nom_voiture, quantite_essence, puissance):
        super().__init__(nom_voiture, quantite_essence)
        self.puissance = puissance
        
### Classe fille de la classe fille (Heritage multiple)


class Avion(voiture):
    def __init__(self, nom_voiture, quantite_essence, puissance):
        super().__init__(nom_voiture, quantite_essence, puissance)

    def se_deplacer(self):
        print("Je me deplace dans les airs")


####

## classe mere 
class ObjetJeu:
    pass

## classe mere

class Arme :
    pass

### classe fille 

class Fusil(Arme, ObjetJeu):
    pass



### Verifier qu'un objet fait partie d'une classe fille
class Animal:
    def __init__(self, nom):
        self.nom = nom
        
    def manger(self):
        print(self.nom, "mange...")
        
class Reptile(Animal):
    def __init__(self, nom, deplacement):
        super().__init__(nom)
        self.deplacement = deplacement
    
    def manger(self):
        print("Le reptile mange...")
        
        
## teste

lezard= Reptile("Lezard","rampe")
lezard.manger()
print(isinstance(lezard, Animal))
print(issubclass(Reptile, Animal))
print("\n\n\n\n\n\n\n\n\n\n\n")





v1 = voiture("Toyota", 2000, "5 cheveaux")
print(v1.montrer_vehicule())
v1.se_deplacer()
v2 = voiture("BMW", 4000, "600 chevaux")
print(v2.montrer_vehicule())

AV =  Avion("Boing 440", "5000 litre de kerozen", "400000 ch")
AV.se_deplacer()