import socket

## se connecter (avec address et port) 
# 127.0.0. = localhost
## chaque client doit avoir un socket
host, port = ('localhost', 5566)
try:
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host, port)) 
    nom = input("Nom :")
    print("Vous êtes connecté")
    nom = nom.encode("utf8")
    socket.send(nom)
    while True:
        
       
        ## envoyer une information  au serveur
        ## travail toujour avec un encodage en utf-8 avant l'envoie et on decode apres reception
        data = input(":")
        ##Encodage
        data = data.encode("utf8")
        ##Envoie du socket
        socket.sendall(data)
    
except ConnectionRefusedError :
    print("Connexion au serveur echouee !")
    
finally:
    socket.close()
