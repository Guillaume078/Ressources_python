
## demarer et ecoute
import socket

""""
##envoie des donnees
##toutes communication passe par le serveur
## elle se demmare avec une address et un port
host, port = ('', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## prend deux arguments obligatoires
## avec ces constante on peut tous faire

##bind prend en parametre ,une address et un port
## Association
socket.bind((host, port))
print("Serveur Demarrer")
## Ecouter 

while True:
    socket.listen(5) ## se Block apres 5 echec de connexion 
    conn, address = socket.accept()
    print("Un client viens de se connecté")
    
    ##Reception de donnee
    data = conn.recv(1024)
    data = data.decode("utf8")
    print(data)
    
conn.close()
socket.close()

## Quand on a des connexion multiple il faut passer par des thread
## Le Serveur est charge de s'occuper des thread
## Exercice application de chat
#------------------------------------------------------------
"""
#------------------------------------------------------------
#### Connexion Multiple
import threading
class ThreadClient(threading.Thread):
    
    def __init__(self, conn):
        threading.Thread.__init__(self)
        self.conn = conn
    
    ## Methode executer lors du lancement du thread    
    def run(self):
        while True:
            data = self.conn.recv(1024)
            data = data.decode("utf8")
            data = data 
            print(data)
             
            

#-----------------------------------------------------------

host, port = ('', 5566)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host, port))
print("Serveur Demarrer")

#-------------------------------------------------------------

while True:
    socket.listen(5)
    conn, address = socket.accept()
    nom = conn.recv(1024)
    nom = nom.decode("utf8")
    print(f"{nom} est connecté")
    myThread =  ThreadClient(conn)
    myThread.start()
    
    
conn.close()
socket.close()











