def welcom():
    print("Bienvenue sur ma chaine")
    resultat = 5 + 6
    print("Le resultat est :", resultat)
    
    
    
year = 2018

def next_year():
    global year
    print("Fin de l'année", year)
    year += 1
    print("Debut de l'année", year)
    
    
### exercice compteur de voyelle
def compteur_voyell(chaine = ""):
    compt = 0
    liste_voyel = ['i','o','y','e','u','a']
    for  i in chaine:
        if i in liste_voyel:
            compt += 1
    return compt        
    

############################################################################################

######## INTERFACE GRAPHIQUE #################

from tkinter import *
import webbrowser

def open_graven_channel():
    webbrowser.open_new("http://youtube.com/gravenilvectuto")

#creer une premiere fenetre 
window  = Tk()
window.title("My apllication")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background='#41b77f')

#Creer la frame
frame  =  Frame(window, bg='#41b77f', bd=1, )#relief=SUNKEN)


##ajouter un premier texte
label_title = Label(frame, text="Bienvenue sur l'application", font=("Courrier", 40), bg='#41b77f', fg="white")
label_title.pack(expand=YES)

label_subtitle = Label(frame, text="Salut !!! a tous", font=("Courrier", 25), bg='#41b77f', fg="white")
label_subtitle.pack(expand=YES)

#Ajouter un premier button
yt_boutton =  Button(frame, text="Ouvrir Youtube", font=("Courrier",25), bg= "white", fg = "#41b77f", command=open_graven_channel )
yt_boutton.pack(pady=25, fill=X)


# ajouter
frame.pack(expand=YES)
window.mainloop()
#afficher
