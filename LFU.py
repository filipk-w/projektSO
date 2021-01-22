import numpy as np, csv

capacity = 7
referenceString = np.random.randint(20, size=1000)
print(referenceString)
memory = {}
recentlyUsed = []
toDelete = []
globalTimer = 0
pageFault = 0
pageHit = 0
usageCounter = 0

for i in referenceString:
    if len(memory) < capacity:
        if i not in memory:
            memory[i] = 1
            print("Fault!",memory)
            pageFault += 1
            recentlyUsed.append(i)
            print(recentlyUsed)
        else:
            memory[i] += 1
            j = recentlyUsed.index(i)
            del recentlyUsed[j]
            recentlyUsed.append(i)
            print("Hit!", memory)
            print(recentlyUsed)
            pageHit +=1
    elif len(memory) >= capacity:
        if i not in memory:
            temp = min(memory.items(), key=lambda x: x[1])
            for item in memory.items():
                if item[1] == temp[1]:
                    toDelete.append(item)
            if len(toDelete) > 1:
                toDelete = sorted(toDelete, key=lambda x: x[1])
                del memory[toDelete[0][0]]
                j = recentlyUsed.index(toDelete[0][0])
                del recentlyUsed[j]
                toDelete = []

            else:
                j = recentlyUsed.index(toDelete[0][0])
                del recentlyUsed[j]
                del memory[toDelete[0][0]]
                toDelete = []

            memory[i] = 1
            recentlyUsed.append(i)
            print(recentlyUsed)
            print("Fault!",memory)
            pageFault += 1
        else:
            j = recentlyUsed.index(i)
            del recentlyUsed[j]
            recentlyUsed.append(i)
            memory[i] += 1
            print("Hit!", memory)
            pageHit += 1
            print(recentlyUsed)
print("Hits:",pageHit,"Faults:",pageFault)