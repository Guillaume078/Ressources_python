import tkinter

"""
StringVar() : chaine de caractere[str]
IntVar      : nombre entier [int]
DoubleVar   : nombre flottant[float]
BooleanVar  : booleen[bool]
"""
"""
#Creation et parametrage de la fenetre..

app = tkinter.Tk()
app.geometry("400x300")
app.title("Variable tkinter")

## fonction observateur (observe et change la valeur de var_label)
def update_label(*args):
    var_label.set(var_entry.get())

#widget
var_label = tkinter.StringVar()
var_entre = tkinter.StringVar()

# trace appelle une fonction lorsque la variable a ete lu ou ecrite
var_entre.trace("w", update_label)

label = tkinter.Label(app, width=30, height=4 , textvariable= var_label )
var_entry = tkinter.Entry(app, textvariable=var_entre)
#change la variable
var_label.set("Label......")

#recupere la variable.
print("label : " , var_label.get())

var_entry.pack()
label.pack()
"""
### pour les widget radiobutton et autre..
 ##----observateur----
def update_observer(*args):
    if var_radio.get():
        var_label.set("C'est un homme ")
    else:
        var_label.set("C'est une femme ")
    
#Creation et parametrage de la fenetre
app2 = tkinter.Tk()
app2.title("Variables tkinter")
var_radio = tkinter.IntVar()
var_radio.trace("w", update_observer)
bouton_radio = tkinter.Radiobutton(app2, text = "Homme" , value= 1, variable= var_radio )
bouton_radio1 = tkinter.Radiobutton(app2, text = "Femme", value = 0,variable= var_radio)


var_label = tkinter.StringVar()
label_var_wideget = tkinter.Label(app2, textvariable= var_label)
bouton_radio.pack()
bouton_radio1.pack()
label_var_wideget.pack()

app2.mainloop()
    


#Boucle principale
##app.mainloop()