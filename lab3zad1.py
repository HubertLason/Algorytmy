def NWD(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a;

def NWDrek(a,b):
    if a!=b:
        if a>b:
            return NWDrek(a-b,b)
        else:
            return NWDrek(a,b-a)
    return a;

def nwdII (a,b):
    while b!=0:
        temp = b
        b = a % b
        a = temp
    return a

def nwdIIrek(a,b):
    if b!=0:
        return nwdIIrek(b,a%b)
    return a