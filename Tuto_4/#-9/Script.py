Y = 4

def afficher(): # la variable global est acccessible en lecture seulement à l'interieur de la fonction
    Y=8         ## Pour pouvoir utiliser une variable global dans une fonction vous devez le definir dans la fonction avec le mot cle (global)
    print(Y)
    
afficher()
print(Y)