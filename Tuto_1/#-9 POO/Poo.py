# creation d'une classe 
class Humain:
    """
     Classe des etres humain
    """
    # espace reserver au attribut de classe 
    humain_creer = 0
    def __init__(self, c_prenom = "toto", c_age=1):
        print("Creation d'un humain")
        # creation d'attribut
        self.prenom = c_prenom
        self.age = c_age
        Humain.humain_creer += 1
    
    # les methodes


print("Lancement du programme... ")
"""
h1 = Humain("jojo")
print("prenom de h1 : {}".format(h1.prenom))
print("Age de h1 : {}".format(h1.age))
h1.prenom = "Guillaume"
print("prenom de h1 : {}".format(h1.prenom))

h2 = Humain("Albert",45)
print("Humain existant : {}".format(Humain.humain_creer))
"""

