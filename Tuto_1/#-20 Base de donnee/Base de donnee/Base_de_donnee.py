## sqllite est fait pour remplacer l'utilisation des fichier texte
## il a etet concue pour fonctionner depuis les telephone, est plus leger que (oracle, mysql)
## il est interdit de lutiliser pour gerer une enorme quantite de donne (des donnee qui vaut des giga octet)
## il n'ya pas de la multiconnexion
###        My sql
### est plus utilise
####      postgre sql
#### est plus puissant que mysql qui permet de gerer des tera octet
##########3##          Gratos          ############

## importation
import sqlite3

## connection
connection = sqlite3.connect("./base.db")

## recuperation de donnee
## creer un curseur permet de travailler avec les requetes
## effectuer une selection (recherche dans la base de donnee)
## les interface CRUD : requete de base (creer, read, update, delete )


cursor = connection.cursor()
## une le curseur prêt on vas travailler avec lui 
## cest avec le curseur on vas pouvoir executer les requetes
## on utilise la methode execute() permet de gerer une information et si plusieur on utiluse executemini()


## lecture
""""
my_username = ("Guillaume",)
req = cursor.execute('SELECT * FROM bk_users WHERE user_name = ?', my_username)
result = cursor.fetchone()[1]
print(f"Le nom de l'utilisateur est : {result}")
"""
"""
### insertion de donnee
## execute() permet passer qu'une seule parametre
## executemany() permet de passer une liste a la requete
new_user = (cursor.lastrowid, "Booba", 23)
cursor.execute('INSERT INTO bk_users VALUES(?,?,?)', new_user)
##enregistrer les nouvelles modification
connection.commit()
print("Nouvel l'utilisateur ajouté !")
"""


##gestion des erreur

try:
    ### recuperation
    req = cursor.execute('SELECT * FROM bk_users')
    for row in req.fetchall():
        print(row[1])

except Exception as e:
    print("Erreur de récupération", e)
    connection.rollback()
finally:
    ## fermer la connection
    connection.close()




## pour revenir au commit precedent
##connection.rollback()











