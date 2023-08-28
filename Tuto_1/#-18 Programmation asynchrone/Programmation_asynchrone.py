from collections.abc import Callable, Iterable, Mapping
import time
import threading
from typing import Any
# par defaut (programmation sequentielle)elle realise lexecution de notre programme de haute en bas

## executer les deux fonction en meme temps de maniere parallele pour cela on utlise les theard() dans le module thearding
## trier et enrgistrer , gerer lanimation et la musique

## possibiliter de placer un verrou(pour eviter de melanger des processus qui se declenche simultannement)

my_lock  =  threading._RLock()

class Myprocess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        
    def run(self):
        i =0 
        while i<3:
            with my_lock:
                letters= "ABC"
                for lt in letters:
                    print(lt)
                    time.sleep(0.3)
            i += 1


def process_one():
    i = 0
    while i <3:
        print("Bonjour  !!")
        time.sleep(0.3)
        i += 1
        
def process_two():
    i = 0
    while i< 3:
        print("Bonsoire !! ")
        time.sleep(0.3)
        i += 1
        
#process_one()
#process_two()
## creation de thread
th1 = Myprocess()
th2 = Myprocess()

th1.start()
th2.start()

th1.join()
th2.join()
print("Fin du programme ")