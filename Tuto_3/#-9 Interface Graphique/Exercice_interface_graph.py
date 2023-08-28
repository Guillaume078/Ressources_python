from tkinter import *

cpt = 0
## Fonction compteur
def compteur():
    global cpt
    cpt += 1
    var_label.set(cpt)
window = Tk()
window.title("Boutique de cookies")
window.geometry("720x480")
window.config(background='#007C94')
window.minsize(420, 380)
#image
height = 300
width = 300
image = PhotoImage(file=("password.png")).zoom(18).subsample(32)


#ceation du frame
frame = Frame(window, bg='#007C94')
frame_bouton = Frame(window,bg='#007C94')
#creation d'un canvas
canvas = Canvas(frame, width=width, height=height, bg='#007C94' , bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image )

## creation du label
var_label = StringVar()
label_compteur = Label(frame, textvariable=var_label,bg='#007C94', fg='white', font=("helvetica", 20)  )
canvas.grid(row=0, column=0, sticky=W)
label_compteur.grid(row=0, column=2, sticky=W)

#creation de bouton
bouton = Button(frame_bouton, text="Ajouter", bg='#007C94', font=("helvetica", 20), fg='white', command=compteur)
bouton_suivant = Button(frame_bouton, text="Suivant", bg='#007C94',font=("helvetica", 20), fg='white')
bouton.pack(side="left", fill=X)
bouton_suivant.pack(side="left", padx=10 , fill=X)
frame.pack(expand= YES)
frame_bouton.pack(side="bottom", pady=25, expand= YES)












window.mainloop()