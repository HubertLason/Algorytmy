def Maximum(A, l, r, max):
    if l==r:
        if max<A[l]:
            max=A[l]
        return max
    b=(l+r)//2
    max=Maximum(A, l, b, max)
    max=Maximum(A, b + 1, r, max)
    return max

tab=[5, 23, 65, 1, 71, 4, 5]
print(Maximum(tab, 0, len(tab)-1,tab[0]))