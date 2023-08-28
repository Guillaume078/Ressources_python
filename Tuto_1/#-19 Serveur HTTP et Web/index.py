from cgi import *


## cgi pour des applications pousser ou un site avance
## fastcgi comme cgi mais excute une seule fois un processus 
print("Content-Type: text/html; charset=utf-8")
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
    <form method="post" action="result.py">
        <p><input type="text" name="Username">
        <input type="submit" value="Envoyer"></p>
    </form>
</body>
</html>
"""

print(html)