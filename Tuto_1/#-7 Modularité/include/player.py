""" 
 module pour joueur
"""

def parler (personnage, message):
    print("{} : {}".format(personnage, message))
    
def au_revoir():
    print("Au revoir merci!!")
    

if __name__ == "__main__":
    
    print("Phase de teste de player.py")
    parler("jason", "Bonjour")
    au_revoir()