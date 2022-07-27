from array import *

tableau=array('i',[1,3,5,3,7,1,9,3])
str(tableau)
for i in tableau:
    if tableau[i]==3:
        del tableau[i]
        break
print(tableau)