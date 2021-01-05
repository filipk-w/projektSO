import random, csv
from typing import Dict, Any

lista = []
i = 10  #ilosc procesow do wygenerowania
for i in range (0, i):
    lista.append(dict(p=i, at=0, bt=0, wt=0))
    lista[i]["bt"] = random.randint(1, 10)  # losowanie burst time
    lista[i]["at"] = random.randint(1, 10)  # losowanie arrival time

print(lista)
with open('test.csv', 'w') as f:
    for i in lista:
        for key in i.keys():
            f.write("%s,%s\n"%(key,i[key]))
#arrival time
#["bt"] = random.randint(1, 10)  #losowanie burst time

