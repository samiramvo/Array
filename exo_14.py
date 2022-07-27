from array import *
tableau=array('i',[2,3,7,8,8])
tableau2=array('i',[3,8,5,4])

def duplicate(tableau):
    tableau_set=set(tableau)
    if len(tableau_set) !=len(tableau):
        return False
    else:
        return False


print(duplicate(tableau))
print(duplicate(tableau2))