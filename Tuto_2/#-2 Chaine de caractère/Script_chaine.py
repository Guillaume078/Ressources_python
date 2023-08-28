
#les fonction split et join
nombre = ("1, 2, 3, 4, 5")
list = nombre.split(", ")
inverse = "- ".join(list)
print(list)
print(inverse)
print(type(inverse))

#la fonction zfill
print("9".zfill(3))

for i in range(100):
    print(str(i).zfill(4))
    
# les methodes <<is>>
b = "bonjour"
nbr = "5"
print(b.islower())
print(nbr.isdigit())

#Compter les occurences
c = "Bonjour le jour"
print("\n",c.count("jour"))
print("\n",c.count(" jour"))

# Trouver une chaine de caractere
print("\n",c.find("jour"))
print("\n",c.index("jour"))

# rechercher au debut et a la fin d'une chaine de caractere
fichier = "image.png"
print("\n",fichier.endswith(".jpg"))
print("\n",fichier.startswith("image"))

# les f-string
age= 14
print(f"Bonjour j'ai {age} ans")
print(f"L'annee prochaine j'aurai {age+1} ans")

# les formats

print("jai {b} ans".format(b=age))
