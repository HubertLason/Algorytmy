import random
import numpy as np

tab = np.random.randint(1,10,(10))

a=int(input("Podaj a: "))

ile=0

for i in range (len(tab)):
    if tab[i]==a:
        ile+=1
print (ile)
