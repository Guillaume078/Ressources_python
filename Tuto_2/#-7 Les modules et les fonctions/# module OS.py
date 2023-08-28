# module OS

import os

chemin = "\\Users\\USER PC\\Documents\\Formation Python\\Apprendre_Python_A_a_Z"
chemin_v = chemin.replace("\\","/")
print(chemin_v)
#creer un dossier
# la fonction join (concatener ce qui dans la variable avec le nom du dossier)
dossier = os.path.join(chemin_v, "Dossier", "test")
print(dossier)
#si le dossier n'existe pas
if not os.path.exists(dossier): 
    os.makedirs(dossier)

# ou
os.makedirs(dossier,exist_ok=true)

# Supprimer un dossier (if mot os.path.exists(dossier) si le dossier existe)
#os.removedirs(dossier)

# pour verifier le systeme d'exploitation
print("1",os.name)