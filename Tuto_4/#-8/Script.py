def signe(A,B):
    if A*B <0:
        print("Les deux valeur sont de signe different")
    else :
        print("Les deux valeur sont de même signe")
def maximum(A,B):
    if A>B :
        return A
    else :
        return B
    
def minimum(A,B):
    if A<B :
        return A
    else:
        return B
    
signe(2,4)
print("Minimum : " , minimum(2,4))
print("Maximum : ", maximum(2,4))