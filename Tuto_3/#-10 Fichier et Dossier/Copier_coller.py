import os
import shutil


source = "password.png"
target = "images/password.png"

shutil.copy(source, target)
#os.remove(source) Supprime le fichier