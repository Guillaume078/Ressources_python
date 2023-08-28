"""A = 0
i = 1
somme = 0
while i <=8:
    A = int(input(f"Entrez N{i} :"))
    if A<0:
        break
    somme+= A
    i += 1
print(somme)
"""
#### Seconde partie l'instruction continue ########

B = 0
som=0
for i in range(1,9):
    print(f"Entrez N{i} :", end="")
    B = int(input())
    if B<0:
        continue
    som +=B
print(som)