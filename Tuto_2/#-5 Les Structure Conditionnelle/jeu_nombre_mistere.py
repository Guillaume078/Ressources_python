from random import randint
print("Le jeu du nombre mystère ***")
nombre = randint(0, 100)
phrase = "Il te reste {fois} essais"
phrase_1 = "Le nombre mystère est {taille} {valeur}"
print(nombre)
i = 0
fo = 5
while i <=5:
    print(phrase.format(fois = fo)) # verifier si cest un nombre qui a ete entree
    reponse = input("Devine le nombre : ")
    if int(reponse) == nombre:
        print(f"Bravo!!! Le nombre mystere etait bien {nombre} ")
        print(f"Tu as trouver le nombre en {6-fo} essai")
        break
    
    elif int(reponse) > nombre:
        print(phrase_1.format(taille= "est plus petit", valeur = reponse))
        fo = fo-1
        continue
    
    elif int(reponse) < nombre:
        print(phrase_1.format(taille = "est plus grand que", valeur = reponse))
        fo = fo -1
        continue
    i = i + 5
    print(f"Dommage ! Le nombre mystere etait {nombre} !")
    
print("Fin du jeu.")