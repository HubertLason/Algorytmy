import numpy as np

def newton(n,k):
    T=np.zeros([n+1,k+1])

    for i in range(n+1):
        for j in range(k+1):
            if (j==0 or j==i):
                T[i][j]=1
            else:
                T[i][j]=T[i-1][j-1]+T[i-1][j]
    return T[n][k]

n=int(input("Podaj n: "))
k=int(input("Podaj k: "))

print(newton(n,k))