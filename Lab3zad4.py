def DzNaBin(a):
   if (a>1):
       DzNaBin(a//2)
   print(a%2, end='')

DzNaBin(16)
print()