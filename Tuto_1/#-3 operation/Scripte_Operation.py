## Operateur binaire
  #-- &
    ##Boolean
x, t  = True, False
y= True
print(x&y, y&t)  # True, False

    ## int
x = 5  # <==> 0b0101
y = 8  # <==> 0b1000
print(x&y) ## 0b0000 <==> 0

  #-- |
    ##Boolean
x, t  = True, False
y= True
print(x|y, y|t)  # True, True
    ## int
x = 5  # <==> 0b0101
y = 8  # <==> 0b1000
print(x|y) ## 0b1101 <==> 13

  #-- ^
    ##Boolean
x, t  = True, False
y, i= True, False
print(x^y, y^t, t^y, t^i)  # False, True, True, False
    ## int
x = 5  # <==> 0b0101
y = 8  # <==> 0b1000
print(x^y) ## 0b1101 <==> 13

  #-- ~
    ##int 
x = 5  # <==> 0b0110
print(~x) ## 0b0110 <==> -6

#-- <<
    ##int 




##Les operateurs d'identité
x = 2
print(x is 2) ## True
print(x is not 2) ##True

##Les operateur d'adhesion
nom = "Guillaume"
print("G" in nom ) ##True
print("Bock" in nom) ## False

##
print((-x) < 0) ## Operateur unitaire..

  
  
