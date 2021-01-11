import random, csv
import numpy as np

from typing import Dict, Any

i = 10  #ilosc procesow do wygenerowania

p = []
at = []
bt = []
for i in range (0, i):
    p.append(i)
    bt.append(np.random.randn(10))


print(lista)
with open('test.csv', 'w') as f:    #zapisanie danych do pliku
    for i in lista:
        for key in i.keys():
            f.write("%s,%s\n"%(key,i[key]))
#arrival time
#["bt"] = random.randint(1, 10)  #losowanie burst time

