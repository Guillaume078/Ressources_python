liste = []
while True : 
    print("""
---------------------------------------------------------------------------
Choisissez parmi les 5 options suivantes :

    1 - Ajouter un element a la liste
    2 - Retirer un element de la liste
    3 - Afficher la liste 
    4 - vider la liste
    5- Quitter 
      """)
    reponse = input("Votre choix :   ")
    if reponse == "1" :
        nom_element = input("Entrer le nom de l'élement à ajouter à la liste de courses : ")
        liste.append(nom_element)
        print(f"L'element {nom_element} a ete ajouter")
        
    elif reponse == "2" :
        nom_element = input("Entrer le nom de l'element à retirer de la liste de courses : ")
        index_element = liste.index(nom_element)
        if liste[index_element] in liste:
            liste.pop(index_element) 
            print(f"l'element {nom_element} a ete supprimer")
        else:
            print(f"L'élement {nom_element} n'est pas dans la liste")
    
    elif reponse == "3":
        if len(liste) == 0:
            print("Votre liste ne contient aucun element")
        else:
            for i in range(len(liste)):
                print(f"{i+1} - {liste[i]} ")
    
    elif reponse == "4":
        liste.clear()
        print("La liste a ete videe de son contenu")
        
    elif reponse == "5":
        print("A bientot !")
        break
   
    else :
        print("Veuillez  choisir une option valide....")
            