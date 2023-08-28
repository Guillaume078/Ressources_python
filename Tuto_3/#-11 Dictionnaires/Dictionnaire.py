import json


eleves = {
    'Paul': {'note': 12, 
             'Appreciation': "passable"},
    'Camille': {'note':18.2,
                'Appreciation' : "Tres bien"} ,
    'Théo' :{'note' : 14,
             'Appreciation' : "Assez-bien"
             }
}

#items()
#values()
#keys
#print(eleves['Paul']['Appreciation'])


#Ajouter

eleves['Lea'] = {'note':10,
                 'Appreciation' : "Peux mieux faire"
                 }

# mofi
eleves['Camille']['note'] = 20

# Verification

if 'Camille' in eleves.keys():
    print("Camille est bien dans la classe")



# suppre

del eleves['Théo']

for eleve in  eleves:
    print(eleve, eleves[eleve]['note'], eleves[eleve]['Appreciation'])


#sauvegarder notre classe dans un fichier

with open("classe.json", "w+") as file:
    json.dump(eleves,file)


##  Charger les donnees depuis le fichier

with open("classe.json", "r") as fil:
    eleves_1 = json.load(fil)

###
#
# Challenge,  non toucher
#
###

"""
for Prenom, valeur in eleves.items():
    print(f"La moyenne de {Prenom} est de {valeur}")

# moyenne de la classe

print(sum(eleves.values())/ len(eleves))
"""
#Affichage
#print(eleves['Paul'])
#print(eleves.get('Lea', 'Prenom'))




