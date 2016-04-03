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
        #b.insert(0, numObs)
        obsA.append(b)
    return obsA
    
def viterbi(example, numberOfA, statesA, observationsA, A, B, pi):
    V = [{}]
    for idx, i in enumerate(statesA):
        V[0][idx] = pi[idx]*B[idx][observationsA.index(example[0])]
    for t in range(1, len(example)):
         V.append({})
         for idx, y in enumerate(statesA):
             prob = max(V[t - 1][idxx]*A[idxx][idx]*B[idx][observationsA.index(example[t])] for idxx, p in enumerate(statesA))
             V[t][idx] = prob
    #for i in dptable(V):
         #print i
    opt = []
    for j in V:
        for x, y in j.items():
            if ((j[x] == max(j.values())) & (j[x] != 0)):
                opt.append(x)
    h = max(V[-1].values())
    return [opt, h]

    
def main():
# print command line arguments
    fileNames = []
    for arg in sys.argv[1:]:
        fileNames.append(arg)
    (a, b, c, d, e, f) = readHMM(fileNames[0])
    k = readEX(fileNames[1])
    for j in k:
        (opt, h) = viterbi(j, a, b, c, d, e, f)
        done = []
        for o in opt:
            done.append(b[o])
        print (str(h) + ' ' + ' '.join(done))

if __name__ == "__main__":
    main()
    