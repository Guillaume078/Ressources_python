from random import randint

user_potion_total = 3
user_point_de_vie = 50
ennemi_point_de_vie = 50

while True :

    user_choice = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? ")
    
    # Verification de la valeur entree
    if not(user_choice.isdigit()):
        continue
    user_choice = int(user_choice)
    # Excution des action en fonction des choix de l'utilisateur
    
    # choix 1 !
    if user_choice == 1 :
        if user_point_de_vie > 0 and ennemi_point_de_vie > 0:
            user_degat = randint(5, 10)
            ennemi_degat = randint(5, 15)
            user_point_de_vie -=  ennemi_degat 
            ennemi_point_de_vie -= user_degat
            print(f"Vous avez inflige {user_degat} points de degats à l'ennemi")
            print(f"L'ennemi vous avez inflige {ennemi_degat} points de degats")
            print(f"il vous reste {user_point_de_vie} point de vie. \n Il reste {ennemi_point_de_vie} points de vie a l'ennemi.")
        elif user_point_de_vie <= 0 and ennemi_point_de_vie > 0:
            print("Game Over !!")
            print(user_point_de_vie, ennemi_point_de_vie)
            break
        elif user_point_de_vie > 0 and ennemi_point_de_vie <= 0:
            print("Bravo !! Vous avez gagne")
            print(user_point_de_vie, ennemi_point_de_vie)
            break
        elif user_point_de_vie == 0 and ennemi_point_de_vie == 0 :
            print("Match null !!")
            print(user_point_de_vie, ennemi_point_de_vie)
            break
        else :
            if user_point_de_vie > 0 and ennemi_point_de_vie < 0:
                if user_point_de_vie > ennemi_point_de_vie:
                    print("Bravo !! Vous avez gagne")
                    break
                else:
                    print("Game Over !!")
                    break
                
    # choix 2 !
    if user_choice == 2 :
    
        if user_point_de_vie > 0 and ennemi_point_de_vie > 0 and user_potion_total > 0:
            user_potion = randint(15, 20)
            ennemi_degat = randint(5, 15)
            user_point_de_vie += user_potion
            user_point_de_vie -= ennemi_degat
            user_potion_total -= 1
            print(f"Vous avez recuperer {user_potion} de point de vie et il vous reste {user_potion_total} potion")
            print(f"L'ennemi vous avez inflige {ennemi_degat} points de degats")
            print(f"il vous reste {user_point_de_vie} point de vie. \n Il reste {ennemi_point_de_vie} points de vie a l'ennemi.")
        if user_point_de_vie <= 0 and ennemi_point_de_vie > 0:
            print("Game Over !!")
            break
        elif user_point_de_vie > 0 and ennemi_point_de_vie <= 0:
            print("Bravo !! Vous avez gagne")
            break
        elif user_point_de_vie == 0 and ennemi_point_de_vie == 0:
            print(user_point_de_vie, ennemi_point_de_vie)
            print("Match null !!")
            break
        else :
            if user_point_de_vie > 0 and ennemi_point_de_vie < 0:
                if user_point_de_vie > ennemi_point_de_vie:
                    print("Bravo !! Vous avez gagne")
                    break
                else:
                    print("Game Over !!")
                    break
            elif user_potion_total == 0:
                print("Vous ne pouver plus prendre de potion")
            
            
    print("-"*50)