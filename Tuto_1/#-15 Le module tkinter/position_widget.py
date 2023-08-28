import tkinter

# Creation et parametrage  de la fenetre

app = tkinter.Tk()
app.geometry("640x488")
app.title("Positionnement widget")

# widgets ...

### widget cadre peut contenir des widget (permet de gerer les widget par groupe)

#mainframe = tkinter.LabelFrame(app, text="Titre" )
#mainframe.pack()


## la methode place()
# place les element a des coordonnees precise pour les option x et y
#relx et rely pour des coordonnees relative.
btn = tkinter.Button(app, text="BIENVENUE")
btn.place(x=10, y=10)


## organiser les element avec grid.
# prend deux option row=  et column=
# les option columnspan= et rowspan=  pour affic(her un widget sur plusieu ligne et commande
#Fonctionne avec padx et pady
# loption sticky = prend(n = nord, s= sud, e = est, w= ouest) 
"""label = tkinter.Label(app, text="Un label")
ent =  tkinter.Entry(app)
btn = tkinter.Button(app, text="BIENVENUE")

label.grid(row=20, column=34)
ent.grid(row= 27, column=10)
btn.grid(row= 0, column= 20)
"""
## la methode pack() permet de placer les widget(Haut, Gauche, en bas, droite) avec la methode side()
#expand  est un boolean prend la valeur (0, 1) pour designe sur le widget est etendu ou non
#possible de coupler les option
#loption fill="y" ou "x"  ou both(vas occuper tous lelement) permet de rempir peut etre coupler avec side
#loption padx = et pady = : pour les marge exterieur
# loption ipadx = et ipadx : pour les marge interieur
"""
label = tkinter.Label(app, text="Un label")
ent =  tkinter.Entry(app)
btn = tkinter.Button(app, text="BIENVENUE")

btn.pack(side="bottom")
label.pack(side="top")
ent.pack(side="top")"""




# Boucle principale 
app.mainloop()