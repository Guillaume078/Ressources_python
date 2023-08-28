# les liste peut contenir differente valeur.
# liste = [1, 2, 3, 4, 5]
#vous pouver melanger nimporte quelle type de variable dans une liste
#une liste est un objet mutable (peut etre modifier)

#Exercice

"""mdp = input("Entrez un mot de passe (min 8 caractères) : ")
mdp_trop_court = "votre mot de passe {mot}"

if mdp == "":
    print(mdp_trop_court.format(mot="est trop court").upper())
elif len(mdp) < 8:
    print(mdp_trop_court.format(mot="mot est trop court").capitalize())
elif mdp.isdigit():
    print(mdp_trop_court.format("ne contient que des nombres").capitalize())
else:
    print("Inscription terminée")
"""
#Exercice sur la comprehension de liste

#----------------Exo1---------------#
nombres = [1, 21, 5, 44, 4, 9, 5, 83, 29, 31, 25, 38]
nombres_pairs = [i for i in nombres if i % 2 == 0]
print(nombres_pairs)

#---------------Exo2----------------#
nombres = range(-10, 10)
nombres_positifs = [i for i in nombres if i >= 0]
print(nombres_positifs)

#---------------Exo3----------------#
nombres = range(5)
nombres_doubles = [i*2 for i in nombres]
print(nombres_doubles)

#---------------Exo4----------------#
nombres = range(10)
nombres_inverses = [i if i % 2 == 0 else -i for i in nombres]  
print(nombres_inverses)

#Exo Afficher dix utilisateur.

for i in range(1, 11):
    print(f"Utilisateur {i}")