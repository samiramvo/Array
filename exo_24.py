from array import array
tableau=array('i',[10,11,12,13,14,16,17,18,19,20])


def manquant(tableau):
    for i in range(10,21):
        for j in tableau:
            if i!=j:
              return i

print(manquant(tableau))