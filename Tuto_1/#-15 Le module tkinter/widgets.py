import tkinter

app = tkinter.Tk()

# le widget bouton
def hello():
    print("Hello world  !!")
button_quit= tkinter.Button(app, text="Envoyer", width=25, height=2, command=hello)

button_quit.pack()




# widget de saisie
#entry_name = tkinter.Entry(app, exportselection=0)
#entry_name = tkinter.Entry(app, width= 20)
#entry_name1 = tkinter.Entry(app, show="*") change ce que vous saisissez en *
#entry_name.pack()

#le premier widget (Label)
#message_welcom = tkinter.Message(app, text="Bonjour tout le monde")
# label_welcom = tkinter.Label(app, text="Bienvenu a tous !")
#label_welcom.configure(text="Nouveau message 2") modification du text du label
#label_welcom["text"] = "Le nouveau message" 
#print(label_welcom.cget("text")) obtenir la valeur dun parametre
#message_welcom.pack()
app.mainloop()