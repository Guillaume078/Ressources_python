## est un fichier text que votre navigateur vas enrgistrer qui permet de stocker une information 
import cgi
import http.cookies ## module qui gere les cookies
##Cookies : SimpleCookie()
import datetime
import os
import sys
## le module de codecs (gere tous ce qui touche a lencodage et le codage)
import codecs
# modification de la sortie standard pour le codage utf-8 (permet dafficher les accents dans le navigateur)
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
# entete de cookies
"""
expires = date
path = chemin
comment = commentaire
domain
secure (utiliser pour une connexion https)
version
htpponly
"""
""""
my_cookie = http.cookies.SimpleCookie() ## fonction comme un dictionnaire

#date
expiration = datetime.datetime.now()+datetime.timedelta(days=365) 
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%S")
#lenregistrement et la creation dun cookie
my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["expires"] = expiration
my_cookie["pref_lang"]["httponly"] = True
print(my_cookie.output())

## doit etre genere avant tous code html
#print("Set-Cookie: pref_lang=fr; httponly")
"""
print("Content-Type: text/html; charset=utf-8\n")


## recuperation d'un cookie

#recup_cookie =[ print(os.environ["HTTP_COOKIE"]) if "HTTP_COOKIE" in os.environ else print("HTTP_COOKIE n'existe pas ")] 
try:
    user_lang= http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print(user_lang["pref_lang"].value)
except (http.cookies.CookieError, KeyError):
    print("non trouver")
    
    
html ="""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Cookies avec python</h1>
    <h3> La langue choisie par l'utilisateur est : {} </h3>
    
</body>
</html>
""".format(user_lang["pref_lang"].value)

print(html)

























