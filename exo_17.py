
tableau=[4,-6,-8,9,7,9,7,0]
def product(tableau):
    if len(tableau)<2:
        print("Nous ne pouvons pas trouver de paire")
    x=tableau[0]
    y=tableau[1]
    for i in range(0,len(tableau)):
        for j in range(i+1,len(tableau)):
            if (tableau[i]*tableau[j]>x*y):
                x=tableau[i]
                y=tableau[j]
    return x,y

print(product(tableau))