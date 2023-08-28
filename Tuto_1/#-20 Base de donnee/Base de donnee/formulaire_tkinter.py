from tkinter import  *

app = Tk()
app.title("Premiere Fenetre")
app.geometry("840x450")

## panneau entry and label
frm_lab_entry = LabelFrame(app, text="User")
Labe_nom = Label(frm_lab_entry, text="Nom :")
entry_nom = Entry(frm_lab_entry)
label_prenom = Label(frm_lab_entry, text="Prenom :")
entry_prnom = Entry(frm_lab_entry)
label_age = Label(frm_lab_entry, text="Age :")
entry_age = Entry(frm_lab_entry)

##panneau de button
frm_btn = LabelFrame(app)
btn1_Ajouter = BooleanVar()
Boutton1 = Button(frm_btn,  text="Ajouter", width=10 , height= 2, bg="green")
btn2_Anuller = BooleanVar()
Boutton2 = Button(frm_btn,  text="Anuller", width=10 , height= 2, bg = "blue")
btn3_supp = BooleanVar()
Boutton3 = Button(frm_btn,  text="Supprimer", width=10 , height= 2, bg = "red")


## Position 

frm_lab_entry.pack(padx=30, pady=20, ipadx=100, ipady=10)
frm_btn.pack(side="bottom" )
Labe_nom.pack()
entry_nom.pack()
label_prenom.pack()
entry_prnom.pack()
label_age.pack()
entry_age.pack()
Boutton1.pack(side="left")
Boutton2.pack(side="left")
Boutton3.pack(side="left")




app.mainloop()