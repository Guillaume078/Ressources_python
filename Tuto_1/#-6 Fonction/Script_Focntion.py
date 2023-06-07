def dire_Bonjour():
    print("Bonjour comment allez-vous??")
   
nom_de_utilisateur ="Guillaume440"
mot_de_pass= "123456"

    
def login(user_name, mot_de_passe):
    if user_name == nom_de_utilisateur and mot_de_pass == mot_de_passe:
        print(f"Bienvenue    {user_name}") 
    else:
        print("erreur de connexion")
        
##nom = input("User name :")
#code =  input("mot de passe :")
#login(nom, code)


## *items

def formulaire(*items):
    nom = items[0]
    prenom = items[1]
    age = items[2]
    print(f"################# \n Nom : {nom}  Prenom : {prenom}  Age : {age}")

##formulaire(input("nom : "), input("Prenom : "), input("Age : "))

## Fonction lambda

x = lambda : print("Bonjour")
print(x())

somme =  lambda x, y : x+y
print(somme(5,3))
