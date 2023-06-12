import numpy as np

def funkcja(n):
    tab=np.zeros([n,n])
    for i in range (n):
        for j in range(n):
            if (j>0 and i==0):
                tab[i][j]=1
            elif (j==0 and i>0):
                tab[i][j]=0
            elif (j>0 and i>0):
                tab[i][j]=(tab[i-1][j]+tab[i][j-1])/2
    return[tab]

n= int(input("Podaj n"))
print(funkcja(n))
