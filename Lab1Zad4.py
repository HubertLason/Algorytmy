import random
import numpy as np

tab = np.random.randint(1,100,(10))
min=tab[0]


for i in range (len(tab)):
    if tab[i]<min:
        min=tab[i]
print (min)
