import csv
from typing import List, Any

procesy = [[]]
queue = [[]]


with open('test.csv', newline='') as plikDanych:
    reader = csv.reader(plikDanych, delimiter=',')
    counter: int = 0
    for row in reader:
        if counter == 0:
            print(f'Column names are {", ".join(row)}')
            counter += 1
        else:

            for i in range(0,3):
                procesy[counter-1].insert(i, row[i])
            procesy.append([])
            counter += 1


print(counter-1)
print(procesy)

globalTimer = 0
finished = True
del queue[0]
#główna pętla programu

while True:
    for i in range(0, counter-1):               #szukanie nowego procesu do kolejki
        if procesy[i][2] == str(globalTimer):
            queue.append(procesy[i])
            print(queue)
    if finished:                                #wybranie obecnie realizowanego procesu
        processTimer = 0
        currentProcess = queue[0]

    if currentProcess[1] == str(processTimer):  #sprawdzam czy zakonczony
        finished = True
        del queue[0]
        print("Finished: ",currentProcess)
    else:
        finished = False

    processTimer += 1
    globalTimer += 1