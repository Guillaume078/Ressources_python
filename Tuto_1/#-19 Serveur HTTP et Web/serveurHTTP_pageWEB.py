import http.server
#import socketserver

"""
## serveur http fonctionnel avec du html (statique)
## le serveur telecharge le fichier html et linterpreter
## port http
port = 80
address = ("",port)
## gere les requete http
handler = http.server.SimpleHTTPRequestHandler #simplehttp
# pour preparer notre serveur
httpd = socketserver.TCPServer(address, handler)
print(f"Serveur demarre sur le PORT {port}")
#boucle infinie
httpd.serve_forever()
"""
## python vas permettre de programmer la partie dynamique du serveur
## pour executer un programme python et l'afficher il vas falloir modifier le serveur et utiliser les interface CGI
port = 80
address = ("", port)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler ## CGI
handler.cgi_directories= ["/"]
## creer le serveur
httpd = server(address,handler)
print(f"Serveur demarré sur le PORT {port}")
httpd.serve_forever()