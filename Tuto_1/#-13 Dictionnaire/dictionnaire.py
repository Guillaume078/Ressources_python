dico = {1:145, "prenom" : "Jason"}

##Ajout
dico["chien"] = "aboie" 
dico["chat"] = "miole" 
dico["lion"] = "rugit" 

##Suppression
valeur_supprimer = dico.pop("chien")
del dico["chat"]

##parcour dun dictio
for key in dico.keys():
    print(key)
print()
for truc in dico.values():
    print(truc)
print()  
for  (k, v) in dico.items():
    print(k," --> ",v)   
    
print(dico)

print(dico["prenom"]) 
