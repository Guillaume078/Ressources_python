import sys
import codecs
import os
import random
# Autre technique
# W+ modifie le fichier
# a+ ajouter le contenus a l'ancien


## Projet Meals
##     Lecture de ce qui se trouve dans le fichier meals
if os.path.exists("Meals.txt"):
    with open("Meals.txt","r+") as file:
        meals_list = file.readlines()
        meals_random_choice = random.choice(meals_list)
        print("Vous propose aujourd'hui : ", meals_random_choice )
        file.close()
        
else:
    print("Le document n'existe pas")
    


















"""
student_list = ["Paul", "Louis", "Mathieu", "Elodie","Aziz","Bernard", "Rachid"]
with open("students.txt", "w+") as file:
    for etudiant in student_list:
        file.write(etudiant +"\n")
    file.close()
"""


"""file = open("students.txt", "w+")
file.write("paul\n")
file.write("edward\n")
file.write("elodi\n")

file.close()
"""