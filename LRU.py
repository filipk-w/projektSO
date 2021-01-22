import numpy as np, csv

capacity = 7
referenceString =  np.random.randint(20, size=1000)
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
            recentlyUsed.append(i)
            print("Recently used:", recentlyUsed)
            pageFault += 1
        else:
            memory[i] += 1
            j = recentlyUsed.index(i)
            del recentlyUsed[j]
            recentlyUsed.append(i)
            print("Recently used:", recentlyUsed)
            print("Hit!", memory)
            pageHit +=1
    elif len(memory) >= capacity:
        if i not in memory:
            del memory[recentlyUsed[0]]
            del recentlyUsed[0]
            recentlyUsed.append(i)
            memory[i] = 1
            print(memory)
            print("Recently used:", recentlyUsed)
            pageFault += 1
        else:
            j = recentlyUsed.index(i)
            del recentlyUsed[j]
            recentlyUsed.append(i)
            print("Recently used:", recentlyUsed)
            memory[i] += 1
            print("Hit!", memory)
            pageHit += 1

print("Hits:",pageHit,"Faults:",pageFault)