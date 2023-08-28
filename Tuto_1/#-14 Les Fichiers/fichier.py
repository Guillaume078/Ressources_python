fic = open("fichier.txt", "r")

# print(fic.read())
print()
print(fic.readline())
print()
print(fic.readlines())


fic.close()
if fic.closed:
    print(" fichier fermé")
else:
    print("toujour ouvert")
    
    
    
    
#### la fonction with (pas besoin de fermer le fichier avec with)

print("la fonction with".center(60, "*"))
with open("fichier.txt", "r") as fich:
    content = fich.read()
    print(content)
    
    
    
##### l'ecriture

print("\n"+"l'ecriture dans un fichier".center(60, "*"))

with open("fichier.txt", "w") as fiche:
    nombre = 15
    fiche.write(str(nombre))
    fiche.write("\nBonjour j'ai reussi a ecrir dans mon fichier.txt\n")
    fiche.write("Et autre....")
    
    
## 
## le module pikle
import pickle

class player :
    def __init__(self, name, level) -> int:
        self.name = name
        self.level = level
    
    def whoami(self):
        print("{}  ({})".format(self.name, self.level))

p1 = player("Guillaume", 20)
with open("Player.data", "wb") as fichier_player:
    record = pickle.Pickler(fichier_player)
    record.dump(p1)
    
print("#"*10)
with open("Player.data", "rb") as fichier_player:
    get_record = pickle.Unpickler(fichier_player)
    player_one = get_record.load()
    
player_one.whoami()