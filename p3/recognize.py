import sys

'''
fileName = 'Z:\\440\P3\sentence.hmm'
fileName2 = 'Z:\\440\P3\example1.obs'
fileName3 = 'Z:\\440\P3\example2.obs'
'''

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
    
def evaluate (example, numberOfA, statesA, observationsA, A, B, pi):
    alpha = []
    for i in range(0, example[0]):
        t = []
        if i == 0:
            for idx, s in enumerate(statesA):
                t.append(pi[idx]*B[idx][observationsA.index(example[i+1])])
            alpha.append(t)
        else:
            for idx, s in enumerate(statesA):
                subtotal = 0
                for idxx, r in enumerate(statesA):
                    subtotal = subtotal + (alpha[i-1][idxx] * A[idxx][idx])
                subtotal = (subtotal * B[idx][observationsA.index(example[i+1])])
                t.append(subtotal)
            alpha.append(t)
    total = 0
    for y in alpha[example[0]-1]:
        total = total + y
    return total
    
'''
(a, b, c, d, e, f) = readHMM(fileName) 
k = readEX(fileName3)
for j in k:
    print (evaluate(j, a, b, c, d, e, f))
    '''
    
def main():
# print command line arguments
    fileNames = []
    for arg in sys.argv[1:]:
        fileNames.append(arg)
    (a, b, c, d, e, f) = readHMM(fileNames[0])
    k = readEX(fileNames[1])
    for j in k:
        print (evaluate(j, a, b, c, d, e, f))

                      
if __name__ == "__main__":
    main()
