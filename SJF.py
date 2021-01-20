import csv

procesy = [[]]
queue = [[]]
zakonczone = [[]]
currentProcess = []
processTimer = 0
timeStarted = 0
timeFinished = 0

def updateQueue():
    for i in range(0, len(procesy)-1):  # szukanie nowego procesu do kolejki
        if (procesy[i][2] == str(globalTimer)) and (procesy[i] not in queue):
            queue.append(procesy[i])



def initialize():
    global currentProcess
    currentProcess = queue[0]
    del queue[0]


def sortQueue():
    if len(queue) >= 2:
        l = len(queue)
        for i in range(0, l):
            for j in range(0, l - i - 1):
                if (queue[j][1] > queue[j + 1][1]):
                    temp = queue[j]
                    queue[j] = queue[j + 1]
                    queue[j + 1] = temp

def processFinished():
    if currentProcess[1] == str(processTimer):  #sprawdzam czy zakonczony
        return True
    else:
        return False

def calculateData():
    waitingTime = globalTimer - processTimer
    currentProcess.append(str(waitingTime))
    currentProcess.append(str(globalTimer))          #zapisanie czasu zakonczenia

def updateTimers():
    global processTimer, globalTimer, timeStarted, timeFinished
    processTimer += 1
    globalTimer += 1
    timeStarted += 1
    timeFinished += 1

def quitProgram():
    if len(queue) == 0:
        return True
    else:
        return False

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

globalTimer = 0
del queue[0]
del zakonczone[0]

updateQueue()
initialize()

while True:                                   #główna pętla programu

    if globalTimer > 0:
        updateQueue()
        print(queue)
    sortQueue()
    if processFinished():
         calculateData()                       #policz wt, end-time
         zakonczone.append(currentProcess)     #dodaj do zakonczonych
         if not len(queue) == 0:
             currentProcess = queue[0]
             del queue[0]
             processTimer = 0

         print("Zakonczone: ", zakonczone)
    if globalTimer>1 and processFinished() and quitProgram():
        with open('wynikiSJF.csv', 'w') as f:  # zapisanie danych do pliku
            f.write("%s,%s,%s,%s,%s\n" % ('pNumber', "burstTime", "arrivalTime","waitingTime","endTime"))
            for i in range(0, counter-1):
                for j in range(0, 5):
                    f.write("%s," % (zakonczone[i][j]))
                f.write("\n")
        break
    updateTimers()