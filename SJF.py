import csv

procesy = [[]]
queue = [[]]
zakonczone = [[]]
currentProcess = []
processTimer = 0
timeStarted = 0
timeFinished = 0
avgWT = 0

def updateQueue():
    for i in range(0, len(procesy)-1):  # szukanie nowego procesu do kolejki
        if (procesy[i][2] == str(globalTimer)) and (procesy[i] not in queue):
            queue.append(procesy[i])



def initialize():
    global currentProcess, processTimer
    if queue[0][2] == str(globalTimer):
        processTimer = 0
        currentProcess = queue[0]
        del queue[0]


def sortQueue():
    global queue
    if len(queue) >= 2:
        queue = sorted(queue, key=lambda x: (int(x[1])))
        # l = len(queue)
        # for i in range(0, l):
        #     for j in range(0, l - i - 1):
        #         if (queue[j][1] > queue[j + 1][1]):
        #             temp = queue[j]
        #             queue[j] = queue[j + 1]
        #             queue[j + 1] = temp

def processFinished():
    if not len(currentProcess) == 0:
        if currentProcess[1] == str(processTimer):
            return True
        else:
            return False

def calculateData():
    waitingTime = globalTimer - processTimer - int(currentProcess[2])
    currentProcess.append(str(waitingTime))
    currentProcess.append(str(globalTimer))

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

def avgWaitingTime():
    global avgWT
    for n in zakonczone:
        avgWT += int(n[3])
    avgWT = avgWT/(counter-1)


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
if len(queue) >= 1:
    initialize()

while True:                                   #główna pętla programu

    if globalTimer > 0:
        updateQueue()
        if len(currentProcess) == 0 and len(queue) >= 1:
            initialize()

    sortQueue()
    print(queue)
    if processFinished():
         calculateData()                       #policz wt, end-time
         zakonczone.append(currentProcess)
         #del queue[0]            #dodaj do zakonczonych
         if not len(queue) == 0:
             currentProcess = queue[0]
             del queue[0]
         elif len(queue) == 0:
             currentProcess = []
         processTimer = 0

         print("Zakonczone: ", zakonczone)
    if globalTimer > 1 and len(zakonczone) == counter-1 and quitProgram():
        avgWaitingTime()
        with open('wynikiSJF_30-5_1000.csv', 'w') as f:  # zapisanie danych do pliku
            f.write("%s%s\n" % ("Sredni czas oczekiwania: ", str(avgWT)))
            f.write("%s,%s,%s,%s,%s\n" % ('pNumber', "burstTime", "arrivalTime","waitingTime","endTime"))
            for i in range(0, counter-1):
                for j in range(0, 5):
                    f.write("%s," % (zakonczone[i][j]))
                f.write("\n")
        break
    updateTimers()