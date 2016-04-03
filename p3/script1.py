fileName = 'Z:\\440\P3\sentence.hmm'
fileName2 = 'Z:\\440\P3\example1.obs'


#Read the hmm file
def readHMM (fileName):
    hmm = open(fileName, 'r')
    numberOf = hmm.readline()
    numberOfA = [0,0,0]
    numberOfA = numberOf.split()
    numberOfA = [int(l) for l in numberOfA]
    states = hmm.readline()
    statesA = ['','','','']
    statesA = states.split()
    observations = hmm.readline()
    observationsA = ['','','','','','','','']
    observationsA = observations.split()
    hmm.readline()
    A = []
    for i in range(0,4):
        a = hmm.readline()
        b = a.split()
        c = [float(l) for l in b]
        A.append(c)
    hmm.readline()
    B = []
    for i in range(0,4):
        a = hmm.readline()
        b = a.split()
        c = [float(l) for l in b]
        B.append(c)
    hmm.readline()
    p = hmm.readline()
    p = p.split()
    pi = [float(l) for l in p]
    return [numberOfA, statesA, observationsA, A, B, pi]
    
def readEX (fileName):
    obs = open(fileName, 'r')
    numDataSets = int(obs.readline())
    obsA = []
    for i in range (0, numDataSets):
        numObs = int(obs.readline())
        a = obs.readline()
        b = a.split()
        b.insert(0, numObs)
        obsA.append(b)
    return obsA
    
def evaluate (example):
    for i in range (0, example[0]):
        
            
