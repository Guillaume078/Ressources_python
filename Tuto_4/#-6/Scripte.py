A = int(input("Veuillez saisir un nombre :"))

while A < 1 or A > 10:
    A = int(input("Veuillez saisir un nombre : "))
i = 0
while  i<=10:
    print(f"{A} * {i} = {A*i}")
    i += 1


########## Deuxieme programme ############

B = int(input("Veuillez entrer un nombre positif superieur a 1 :"))

while B < 1 :
    B = int(input("Veuillez entrer un nombre positif superieur a 1 :"))

i = B
while i >= 1:
    B += i-1  
    i -= 1
print(B)  








