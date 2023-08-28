import tkinter

mainApp = tkinter.Tk()
mainApp.title("Premiere fenetre")

#centreer la fenetre
screenx =int(mainApp.winfo_screenwidth())
screeny=int (mainApp.winfo_screenheight())
WindowsX=400
WindowsY=200
posX = (screenx//2) - (WindowsX//2)
posY = (screeny//2) - (WindowsY//2)
geo = "{}x{}+{}+{}".format(WindowsX,WindowsY,posX,posY)
mainApp.geometry(geo)
# mainApp.sizefrom("user")
# mainApp.positionfrom("user")



#mainApp.minsize(640, 480)
#mainApp.maxsize(1820, 720)
#mainApp.resizable(width=False, height=False) #empecher le redimmensionnement

# mainApp.geometry("800x600+10+100")



mainApp.mainloop()