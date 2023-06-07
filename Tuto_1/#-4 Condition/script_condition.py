
def Verif_age(age):
    if age <= 7:
        print("Vous êtes un bébé")
    elif 7 <= age <= 14:
        print("Vous êtes un ado")
    elif 15<= age <= 18:
        print("Vous Etes un mineur")
    elif 19<= age <= 23:
        print("Vous êtes un majeur")
    else:
        print("Vous êtes un adulte")
        
        
Verif_age(2)
Verif_age(12)
Verif_age(16)
Verif_age(19)
Verif_age(30)
