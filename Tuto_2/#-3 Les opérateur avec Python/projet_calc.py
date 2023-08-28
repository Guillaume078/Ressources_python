while True :
    nombre_1 = input("Entrer un premier nombre : ")
    nombre_2 = input("Entrer un deuxieme nombre : ")
    if not(nombre_1.isdigit() and nombre_2.isdigit()):
        print("Entrer deux nombres valides ")
    else:
        break

print(f"Le resultat de laddition de {nombre_1} avec {nombre_2} est egal a {int(nombre_1)+int(nombre_2)}")