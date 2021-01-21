import numpy as np, csv

capacity = 3
referenceString =  np.random.randint(4, size=10)
print(referenceString)
memory = {}
recentlyUsed = []
globalTimer = 0
pageFault = 0
pageHit = 0

for i in referenceString:
    if len(memory) < capacity:
        if i not in memory:
            memory[i] = 1
            print(memory)
            pageFault += 1
        else:
            memory[i] += 1
            print("Hit!", memory)
            pageHit +=1
    elif len(memory) >= capacity:
        if i not in memory:
            del memory[min(memory, key=lambda k: d[k])]
            memory[i] = 1
            print(memory)
            pageFault += 1
        else:
            memory[i] += 1
            print("Hit!", memory)
            pageHit += 1

print("Hits:",pageHit,"Faults:",pageFault)