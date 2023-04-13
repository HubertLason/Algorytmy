def dyn(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    elif n>1:
        T=[1,1]
        i=2
        while(i<=n):
            T.append(2*T[i-1]-T[i-2])
            i+=1
        return T[-1]

n=int(input("Podaj n: "))

if (n>0):
    print(dyn(n))
else:
    print("Podano złe dane")