nombre2 = input("entrer un nombre:")

try:
    nombre2 = int(nombre2)
    # on peut preciser le type d'erreur
except ZeroDivisionError:
    print("Vous ne povez pas diviser par zéro.")
    
except ValueError:
    print("vous devez entrer un nombre.")

except:
    print("Valeur incorrecte")

else:
    print("Bravo tu as note un nombre valide")
    
finally:
    print("Fin du programme...")
    
# lever un exception

age = input("Quel age as-tu ?")
age = int (age)

if age < 25:
    raise ("coucou:) !")

# comment gerer tous ce qui est une assertion
#Une assertion teste un code ou il peut y avoir un souci

try :
    age = input("Quel age as-tu ?")
    age = int(age)
    
    assert age < 25 # je veux que age soit plus grand que 25
    
except AssertionError: 
    print("J'ai attrape l'exception")
    
 