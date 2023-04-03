def Suma(A, l, r):
    if l==r:
        return A[l]
    else:
        b=(l+r)//2
        S1=Suma(A,l,b)
        S2=Suma(A,b+1,r)
        return S1+S2

tab=[10,20,30,50]
print (Suma(tab, 0, len(tab)-1))