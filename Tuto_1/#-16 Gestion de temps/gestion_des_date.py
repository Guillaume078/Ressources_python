import datetime
##datetime prend en compte la date et le temps
d1 = datetime.datetime(2023, 5, 23, 11, 47, 12)
d2 = datetime.datetime(2023, 6, 1, 11, 47, 12)
## la fonction permet de travailler uniquement avec la date
d3 =datetime.date(2023, 2, 7)
## date est une classe qui gere que la date
## time pour ne minipuler que le temps
## la fonction now() est dans la classe datetime qui est dans le module datetime : retourne le temps actuel
## la fonction today() dansla classe date permet la date du jour
## var_dat.Year()
## comparaison des dates
"""
if d1 < d2 :
    print("d1 est plus acien que d2")
else:
    print("d1 est plus recent que d2")
"""    