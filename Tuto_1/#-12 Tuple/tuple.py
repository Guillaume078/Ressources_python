tupl = ()
tupl = 17,

## affectation multiple
def get_player_position():
    posx = 34
    posy = 234
    return(posx, posy)

##programme principale

cordX = 0
cordY = 0
print("position du jouer : ({})/({})".format(cordX, cordY))
(cordX, cordY) = get_player_position()
print("position du jouer : ({})/({})".format(cordX, cordY))
cordX = 12
cordY = 34

print("position du jouer : ({})/({})".format(cordX, cordY))