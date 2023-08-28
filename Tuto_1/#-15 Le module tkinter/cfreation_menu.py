import tkinter


## les methode pour les menu 
##    add_checkbox()
##    add_radion_button()
##    add_separator()


## creation de la fenetre + parametre

app = tkinter.Tk()
app.geometry("640x480")
app.title("Création de Menu")

#widgets
### widget toplevel permet de faire de s fenetre supplementaire
def show_about():
    about_window = tkinter.Toplevel(app)
    about_window.title("A propos")
    lb =tkinter.Label(about_window, text=("Bonjour !!"))
    lb.pack()
## widget de menu (barre de menu composer de Menu et chacun des menu contient des sous menu)
def hello():
    print("Bonjour !!")
    
main_menu = tkinter.Menu(app)
# element 1
first_menu = tkinter.Menu(main_menu, tearoff=0)
first_menu.add_command(label="Option1", command=hello)
first_menu.add_command(label="Option2")
first_menu.add_command(label="Option3")
first_menu.add_command(label="Afficher", command=show_about)
#element 2
twice_menu = tkinter.Menu(main_menu, tearoff=0)
twice_menu.add_command(label="Commande 1")
twice_menu.add_command(label="Commande 2")
twice_menu.add_command(label="Commande 3")
twice_menu.add_command(label="Commande 4")

main_menu.add_cascade(label="Premier", menu=first_menu)
main_menu.add_cascade(label="Deuxieme", menu= twice_menu)


app.config(menu=main_menu)
#boucle principale
app.mainloop() 