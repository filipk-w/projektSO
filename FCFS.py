import csv
from typing import List, Any

procesy: list[list[Any]] = [[]]

with open('test.csv', newline='') as plikDanych:
    reader = csv.reader(plikDanych, delimiter=',')
    counter: int = 0
    for row in reader:
        if counter == 0:
            print(f'Column names are {", ".join(row)}')
            counter += 1
        else:

            for i in range(0,3):
                procesy[counter-1].append(row[i])
            procesy.append([])
            counter += 1


print(counter-1)
print(procesy)

globalTimer = 0

#główna pętla programu
#while True:
#    currentProcess =

#    globalTimer += 1