from tkinter import *
import string
import random

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits
    
    password ="".join(random.choice(all_chars) for x in range(random.randint(password_min, password_max)))
    passwor_entry.delete(0, END)
    passwor_entry.insert(0,password)
    
#creer la fenetre 

window =Tk()
window.title("Generateur de mot de passe")
window.geometry("720x480")
window.iconbitmap("logo.ico")
window.config(background='#4065A4')
# creer la frame principale
frame = Frame(window,bg='#4065A4')


#creation d'image
width = 300
heigth = 300
image = PhotoImage(file="password (2).png").zoom(18).subsample(32)
canvas = Canvas(frame, width=width, height=heigth, bg='#4065A4', bd=0, highlightthickness=0)
canvas.create_image(width/2, heigth/2, image=image)
canvas.grid(row=0, column=0, sticky=W)
#creer une sous boite
right_frame = Frame(frame, bg='#4065A4')

#creer un titre
label_title = Label(right_frame, text="Mot de passe", font=("helvetica", 20), bg='#4065A4', fg='white')
label_title.pack()
#creer un champ /entree/ input
passwor_entry = Entry(right_frame, font=("helvetica", 20), bg='#4065A4', fg='white' )
passwor_entry.pack()
#creer un bouton
generate_password_button = Button(right_frame, font=("helvetica", 20), text= "Générer", bg='#4065A4', fg='white', command= generate_password)
generate_password_button.pack(fill=X)

#creation d'une barre de menu
menu_bar = Menu(window)
#creer un premier menu 
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier",menu=file_menu)

#configurer notre fenetre pour ajouter cette menu bar
window.config(menu=menu_bar)

right_frame.grid(row=0, column=1, sticky= W) 
frame.pack(expand=YES)

















#Afficher la fenetre
window.mainloop()