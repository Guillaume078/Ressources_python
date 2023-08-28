import tkinter
from tkinter import messagebox
#app = tkinter.Tk()

#les messagebox
"""
    showerror
    Showinfo
    showwarning
    askquestion
    askokcancel
    askyesno
    askretrycancel
"""

def  show_modal_window():
    messagebox.showerror("Erreur", "Un probleme est survenu !")

app1 = tkinter.Tk()
btn = tkinter.Button(app1 , text="Declencher une erreur", command= show_modal_window)

btn.pack()




app1.mainloop()
"""
# widget la liste box
list_box = tkinter.Listbox(app)
list_box.insert(1,"windows")
list_box.insert(2,"Gnu/Linux")
list_box.pack()

# le widget spinbox.
spin_widget = tkinter.Spinbox(app, from_=1 , to=10)
spin_widget.pack()

# les widget de type cursseur
scale_widg = tkinter.Scale(app, from_=10, to=100, tickinterval=25) #changer la fourchette de valeur, tic pour la graduation
scale_widg.pack()







#widget de type radio
radio_widget = tkinter.Radiobutton(app, text="homme", value=1)
radio_widget1 = tkinter.Radiobutton(app, text="femme", value=0)
radio_widget.pack()
radio_widget1.pack()

# le widget checkbox
check_widget = tkinter.Checkbutton(app, text="Publier ?", offvalue=2, onvalue=5, height=2 , width=5)
check_widget.pack()
app.mainloop()"""