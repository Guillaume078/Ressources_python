import time

## la fonction sleep permet de suspendre un processus
##time.sleep(5)
##print(time.time()) donne le temps actuellement depuis 1970, 00h00
##          localtime()
## (TIMESTAMP)-------> Structure de temps
###          <---------
###         mktime()
"""
begin = time.time()
print("Debut")
time.sleep(5)
end = time.time()
print("Fin")
print(f"Temps execute :{end-begin}")"""

### La fonction time.strftime() : Avoir du chaine pour manipuler du temps
## %d : jour (01 a 31)
## %m : mois
## %Y : annee
## %H : heures(OO a 23)
## %I : minutes
## %S : secondes
## %p : AM/PM
## %A : jour semaine / %a (jour abrege)
## %B : mois / %b (mois abrege)
## %Z : fuseau horaire (timezone)

print(time.strftime("%Y-%m-%d"))