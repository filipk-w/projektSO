import csv

#deklaracje niezbednych zmiennych
procesy = [[]]
queue = [[]]
zakonczone = [[]]
currentProcess = []
processTimer = 0
timeStarted = 0
timeFinished = 0
avgWT = 0

def updateQueue():                              #szukanie nowego procesu do kolejki
    for i in range(0, counter-1):
        if procesy[i][2] == str(globalTimer):
            queue.append(procesy[i])
            print(queue)

def initialize():
    global currentProcess, processTimer
    if len(queue) != 0 and queue[0][2] == str(globalTimer):
        currentProcess = queue[0]
        processTimer = 0

def processFinished():                          #sprawdzenie czy wykonywany proces juz sie zakonczyl
    if not len(currentProcess) == 0:
        if currentProcess[1] == str(processTimer):
            del queue[0]
            return True
        else:
            return False

def calculateData():                            #obliczanie czasu oczekiwania i zapisanie go
    waitingTime = globalTimer - processTimer - int(currentProcess[2])
    currentProcess.append(str(waitingTime))
    currentProcess.append(str(globalTimer))     #zapisanie czasu zakonczenia procesu

def updateTimers():                             #obsługa liczników
    global processTimer, globalTimer, timeStarted, timeFinished
    processTimer += 1
    globalTimer += 1
    timeStarted += 1
    timeFinished += 1

def quitProgram():                              #sprawdzenie czy można zakonczyć dzialanie programu
    if len(queue) == 0 and len(zakonczone) >= counter-1:
        return True
    else:
        return False

def avgWaitingTime():
    global avgWT
    for n in zakonczone:
        avgWT += int(n[3])
    avgWT = avgWT/(counter-1)


with open('test.csv', newline='') as plikDanych:            #wczytanie danych do testu z pliku
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

#główna pętla programu
while True:

    updateQueue()
    initialize()

    if quitProgram():
        avgWaitingTime()
        with open('wynikiFCFS_30-5_1000.csv', 'w') as f:  # zapisanie danych do pliku
            f.write("%s%s\n" % ("Sredni czas oczekiwania: ",str(avgWT)))
            f.write("%s,%s,%s,%s,%s\n" % ('pNumber', "burstTime", "arrivalTime","waitingTime","endTime"))
            for i in range(0, counter-1):
                for j in range(0, 5):
                    f.write("%s," % (zakonczone[i][j]))
                f.write("\n")
        break

    if processFinished():
        calculateData()
        zakonczone.append(currentProcess)     #dodaj do zakonczonych
        if not len(queue) == 0:
            currentProcess = queue[0]
        processTimer = 0
        print("Zakonczone: ", zakonczone)

    updateTimers()