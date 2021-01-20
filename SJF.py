import csv

procesy = [[]]
queue = [[]]
zakonczone = [[]]
currentProcess = []
processTimer = 0
timeStarted = 0
timeFinished = 0

def updateQueue():
    temp = procesy[0]
    for i in range(0, counter-1):               #szukanie nowego procesu do kolejki
        if procesy[i][1] < temp[1]:
            temp = procesy[i]
        queue.append(procesy[i])
        print(queue)

def initialize():
    global currentProcess
    if not len(queue) == 0:
        currentProcess = queue[0]

def processFinished():
    if currentProcess[1] == str(processTimer):  #sprawdzam czy zakonczony
        del queue[0]
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


while True:                                   #główna pętla programu

    updateQueue()
    initialize()

    if quitProgram():
        with open('wynikiFCFS.csv', 'w') as f:  # zapisanie danych do pliku
            f.write("%s,%s,%s,%s,%s\n" % ('pNumber', "burstTime", "arrivalTime","waitingTime","endTime"))
            for i in range(0, counter-1):
                for j in range(0, 5):
                    f.write("%s," % (zakonczone[i][j]))
                f.write("\n")
        break

    if processFinished():
        calculateData()                       #policz wt, end-time
        zakonczone.append(currentProcess)     #dodaj do zakonczonych
        if not len(queue) == 0:
            currentProcess = queue[0]
        processTimer = 0
        print("Zakonczone: ", zakonczone)

    updateTimers()