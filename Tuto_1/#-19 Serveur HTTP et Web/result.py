import cgi
import cgitb

## on peut associer les page html et du code python au niveau des formulaire
##mode debug  activer//commenter ou retirer lorsque votre site est en ligne(activer en developpement)
cgitb.enable()
## demarer la recup des donnees
form = cgi.FieldStorage()

if form.getvalue("Username"):
    ##recupere la chaine tape dans le formulaire
    username = form.getvalue("Username")
else:
    raise Exception("Pseudo non transmis")

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
    <h1>Page Web avec python CGI</h1>
    <h3> Bonjour {} </h3>
</body>
</html>
""".format(username)

print(html)

## pour la securiter vous pouvez utiliser les methodes dans un chaine de cractere